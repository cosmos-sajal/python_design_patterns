## refernces - https://www.youtube.com/watch?v=MOEsKHqLiBM

from abc import ABCMeta, abstractmethod


class Movement(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass


class Fly(Movement):
    def move(self):
        print("I will fly")


class Walk(Movement):
    def move(self):
        print("I will walk")


class Swim(Movement):
    def move(self):
        print("I will swim")


class Animal():
    def __init__(self, name):
        self.name = name
        self.movement = ""

    def get_movement(self):
        self.movement.move()

    def set_movement(self, movement):
        self.movement = movement

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Bhow")


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("no sound")


class Eagle(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("chi chi")


animal_type = int(input(
    "What kind of animal are you? \n 1. Dog 2. Fish 3. Eagle? "))
if animal_type == 1:
    animal = Dog("Buzo")
    animal.set_movement(Walk())
elif animal_type == 2:
    animal = Fish("fish_name")
    animal.set_movement(Swim())
else:
    animal = Eagle("Eagle Name")
    animal.set_movement(Fly())

animal.get_movement()
animal.make_sound()
