from components.ai import HostileEnemy
from components.fighter import Fighter
from components import consumable # This
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, base_defense=0, base_power=4),
    level=Level(level_up_base=200),
    sound="sound_effects/melee.wav"
)

# Enemies

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=8, base_defense=0, base_power=1),
    level=Level(xp_given=35),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    level=Level(xp_given=100),
)

# Potions

coin = Item(
    char='*',
    color=(255,255,0),
    name="Coin",
    consumable=consumable.CoinConsumable()
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name = "Health Potion",
    consumable=consumable.HealingConsumable(amount=6),
)