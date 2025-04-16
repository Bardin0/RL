from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import actions
import color
from components.base_component import BaseComponent
import components.inventory
from input_handlers import ActionOrHandler # This
from exceptions import Impossible

if TYPE_CHECKING:
    from entity import Actor, Item

class Consumable(BaseComponent):
    parent: Item

    def get_action(self, consumer: Actor) -> Optional[ActionOrHandler]:
        """Try to return the action for this item."""
        return actions.ItemAction(consumer, self.parent)

    def activate(self, action: actions.ItemAction) -> None:
        """Invoke this items ability.

        `action` is the context for this activation.
        """
        raise NotImplementedError()

class HealingConsumable(Consumable):
    def __init__(self, amount: int):
        self.amount = amount

    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        amount_recovered = consumer.fighter.heal(self.amount)

        self.engine.message_log.add_message(
            f"You consume the {self.parent.name}, and recover {amount_recovered} HP!",
            color.health_recovered,
        )

              
class CoinConsumable(Consumable):

    def activate(self, action: actions.ItemAction):
        self.engine.message_log.add_message(f"You picked up the Coin!")