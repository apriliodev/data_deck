from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidStrategy, BattleStrategy


flame_factory = FlameFactory()
aqua_factory = AquaFactory()
heal_factory = HealingCreatureFactory()
transform_factory = TransformCreatureFactory()

normal = NormalStrategy()
aggressive = AggressiveStrategy()
defensive = DefensiveStrategy()


def battle(op: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(op)} opponents involved\n")
    for i in range(len(op)):
        for j in range(i + 1, len(op)):
            factory1, strategy1 = op[i]
            factory2, strategy2 = op[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
            except InvalidStrategy as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            if not (i == len(op) - 2 and j == len(op) - 1):
                print()


opponents = [
    (aqua_factory, normal),
    (heal_factory, defensive),
    (transform_factory, aggressive)
]
if __name__ == "__main__":
    op = [
        (flame_factory, normal),
        (heal_factory, defensive)
    ]
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(op)
    op = [
        (flame_factory, aggressive),
        (heal_factory, defensive)
    ]
    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(op)
    op = [
        (aqua_factory, normal),
        (heal_factory, defensive),
        (transform_factory, aggressive)
    ]
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(op)
