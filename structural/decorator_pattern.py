# https://stackoverflow.com/questions/3477962/when-do-we-need-decorator-pattern
# https://stackoverflow.com/questions/1549743/when-to-use-the-decorator-pattern/37504043#37504043

from abc import ABCMeta, abstractmethod


class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class ThinDoughPlainPizza(Pizza):
    def get_description(self):
        return "Thin Dough"

    def get_cost(self):
        return 100.00


class CheeseBurstDoughPizza(Pizza):
    def get_description(self):
        return "Cheese Burst Dough"

    def get_cost(self):
        return 160.00


class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.temp_pizza = pizza

    def get_description(self):
        return self.temp_pizza.get_description()

    def get_cost(self):
        return self.temp_pizza.get_cost()


class Cheese(PizzaDecorator):
    def __init__(self, pizza):
        super(Cheese, self).__init__(pizza)

    def get_description(self):
        return self.temp_pizza.get_description() + " Cheese"

    def get_cost(self):
        return self.temp_pizza.get_cost() + 30.00


class Capsicum(PizzaDecorator):
    def __init__(self, pizza):
        super(Capsicum, self).__init__(pizza)

    def get_description(self):
        return self.temp_pizza.get_description() + " Capsicum"

    def get_cost(self):
        return self.temp_pizza.get_cost() + 20.00


class TomatoSauce(PizzaDecorator):
    def __init__(self, pizza):
        super(TomatoSauce, self).__init__(pizza)

    def get_description(self):
        return self.temp_pizza.get_description() + " Tomato Sauce"

    def get_cost(self):
        return self.temp_pizza.get_cost() + 40.00


pizza = TomatoSauce(Capsicum(Cheese(ThinDoughPlainPizza())))
print(pizza.get_description())
print(pizza.get_cost())

pizza = TomatoSauce(Cheese(TomatoSauce(ThinDoughPlainPizza())))
print(pizza.get_description())
print(pizza.get_cost())

pizza = TomatoSauce(Capsicum(Cheese(CheeseBurstDoughPizza())))
print(pizza.get_description())
print(pizza.get_cost())
