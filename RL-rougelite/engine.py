from __future__ import annotations

from typing import TYPE_CHECKING

from tcod.console import Console
from tcod.map import compute_fov

from message_log import MessageLog
import render_function
from components.fighter import Fighter
import entity_factories
from components.level import Level
import math

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap, GameWorld

class Engine:
    game_map: GameMap
    game_world: GameWorld

    def __init__(self, player: Actor):
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                try:
                    entity.ai.perform()
                except Exception:
                    pass

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console) -> None:
        self.game_map.render(console)

        self.message_log.render(console=console, x=21, y=45, width=40, height=5)

        render_function.render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )

        render_function.render_dungeon_level(
            console=console,
            dungeon_level=self.game_world.current_floor,
            location=(0, 47),
        )

        render_function.render_names_at_mouse_location(
            console=console, x=21, y=44, engine=self
        )

    def update_stats(self):
        entity_factories.orc.fighter = Fighter(
                                        hp=8+(self.game_world.current_floor), 
                                        base_defense= 0+(self.game_world.current_floor//2), 
                                        base_power=1+(self.game_world.current_floor//2))
        entity_factories.orc.level = Level(xp_given=(math.ceil(35+(self.game_world.current_floor * 1.2))))
        entity_factories.orc.fighter.parent = entity_factories.orc

        if self.game_world.current_floor > 3:
            entity_factories.troll.fighter = Fighter(
                                        hp=16+(self.game_world.current_floor), 
                                        base_defense= 1+(self.game_world.current_floor//2), 
                                        base_power=4+(self.game_world.current_floor//2))
            entity_factories.troll.level = Level(xp_given=(math.ceil(100+(self.game_world.current_floor * 1.2))))
            entity_factories.troll.fighter.parent = entity_factories.troll

        

        

        