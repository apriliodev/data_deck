from ex0 import FlameFactory, AquaFactory, CreatureFactory

def show_creature(object):
    base = object.create_base()
    print("Testing factory")
    print(base.describe())
    print(base.attack())

    evolved = object.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def creature_fight(factory1: CreatureFactory, factory2: CreatureFactory):
    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(base1.describe())
    print("vs.")
    print(base2.describe())
    print("fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":

    show_creature(FlameFactory())
    print("\n")
    show_creature(AquaFactory())
    print("\n")
    print("Testing battle")
    creature_fight(FlameFactory(), AquaFactory())