from ex1 import HealingCreatureFactory, TransformCreatureFactory


def heal_factory(object):
    base = object.create_base()
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print("evolved:")
    evolved = object.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def transform_factory(object):
    base = object.create_base()
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    evolved = object.create_evolved()
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    heal_factory(HealingCreatureFactory())
    print("\n")
    print("Testing Creature with transform capability")
    transform_factory(TransformCreatureFactory())
