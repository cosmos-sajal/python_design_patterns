# https://stackify.com/design-patterns-explained-adapter-pattern-with-code-examples/
# https://stackoverflow.com/questions/1673841/examples-of-gof-design-patterns-in-javas-core-libraries

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def run(self):
        pass

    def eat(self):
        pass


class Dog(Animal):
    def run(self):
        print("Dog is running")

    def eat(self):
        print("Dog is eating food")


class SpaceShip():
    def fly(self):
        print("Space ship is flying")

    def refuel(self):
        print("Refueling engine")


class SpaceShipAdapter(Animal):
    def __init__(self, space_ship):
        self.space_ship = space_ship

    def run(self):
        self.space_ship.fly()

    def eat(self):
        self.space_ship.refuel()


dog = Dog()
dog.run()
dog.eat()

space_ship_adapter = SpaceShipAdapter(SpaceShip())
space_ship_adapter.run()
space_ship_adapter.eat()
