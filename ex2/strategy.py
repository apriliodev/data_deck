from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import TransformCapability, HealCapability
from typing import cast


class InvalidStrategy(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return f"{creature.attack()}"


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}'"
                "for this aggressive strategy"
            )
        transform_creature = cast(TransformCapability, creature)
        m1 = transform_creature.transform()
        m2 = creature.attack()
        m3 = transform_creature.revert()
        return f"{m1}\n{m2}\n{m3}"


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}'"
                "for this defensive strategy"
            )
        heal_creature = cast(HealCapability, creature)
        m1 = creature.attack()
        m2 = heal_creature.heal()
        return f"{m1}\n{m2}"
