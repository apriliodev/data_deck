from abc import ABC, abstractmethod
from ex0.creature import Flameling, Pyrodon, Aquabub, Torragon, Creature

class CreatureFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
