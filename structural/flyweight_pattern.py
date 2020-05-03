# https://refactoring.guru/design-patterns/flyweight

from tkinter import *
import random

master = Tk()
w = Canvas(master, width=2000, height=2000)
w.pack()


class FlyweightFactory():
    def __init__(self, start_x, start_y, end_x, end_y, colour):
        self._start_x = start_x
        self._start_y = start_y
        self._end_x = end_x
        self._end_y = end_y
        self._colour = colour

    def draw(self):
        w.create_rectangle(self._start_x, self._start_y,
                           self._end_x, self._end_y, fill=self._colour.get_colour())


class Flyweight():
    def __init__(self, colour):
        self._colour = colour

    def get_colour(self):
        return self._colour


def get_random_int():
    numbers = "1234567890"

    return int(''.join(random.choice(numbers) for i in range(3)))


colours = ["red", "green", "blue", "orange", "black"]
colour_dict = {}
for i in range(100000):
    colour = random.choice(colours)
    start_x = get_random_int()
    start_y = get_random_int()
    end_x = get_random_int()
    end_y = get_random_int()
    if colour in colour_dict:
        colour_obj = colour_dict[colour]
    else:
        colour_obj = Flyweight(colour)
        colour_dict[colour] = colour_obj

    rectangle = FlyweightFactory(start_x, start_y, end_x,
                                 end_y, colour_obj)
    rectangle.draw()

mainloop()
