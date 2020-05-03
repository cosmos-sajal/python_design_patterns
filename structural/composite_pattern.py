# https://refactoring.guru/design-patterns/composite/python/example

from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    def add(self, component):
        pass

    def remove(self, component):
        pass

    @abstractmethod
    def calculate(self):
        pass


class Leaf(Component):
    def __init__(self, value):
        self._value = value

    def calculate(self):
        return self._value


class Composite(Component):
    def __init__(self, value):
        self._value = value
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def calculate(self):
        total_value = self._value
        for child in self._children:
            total_value += child.calculate()

        return total_value


composite_1 = Composite(100.0)
composite_2 = Composite(10.0)
composite_3 = Composite(20.0)
composite_4 = Composite(5.0)
composite_5 = Composite(25.0)
composite_6 = Composite(15.0)

leaf_1 = Leaf(1340.0)
leaf_2 = Leaf(1500.0)
leaf_3 = Leaf(1230.0)
leaf_4 = Leaf(1230.0)
leaf_5 = Leaf(1130.0)
leaf_6 = Leaf(1330.0)
leaf_7 = Leaf(1430.0)
leaf_8 = Leaf(1530.0)
leaf_9 = Leaf(1630.0)

composite_1.add(composite_2)
composite_1.add(composite_3)
composite_1.add(leaf_1)

composite_2.add(composite_4)
composite_2.add(composite_5)
composite_2.add(composite_6)

composite_3.add(leaf_2)
composite_3.add(leaf_3)

composite_4.add(leaf_4)
composite_4.add(leaf_5)
composite_4.add(leaf_6)

composite_5.add(leaf_7)
composite_5.add(leaf_8)

composite_6.add(leaf_9)

total_value = composite_1.calculate()
print(total_value)
