# Задание мне немного не понятно. Что необходимо сделать?
from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def get_rashod(self):
        pass


class Topcoat(Wear):

    def __init__(self):
        self.__size = 0

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 0:
            self.__size = 0
        else:
            self.__size = value

    def get_rashod(self):
        return self.__size / 6.5 + 0.5


class Costume(Wear):

    def __init__(self):
        self.__growth = 0

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, value):
        if value < 0:
            self.__growth = 0
        else:
            self.__growth = value

    def get_rashod(self):
        return 2 * self.__growth + 0.3


p1 = Topcoat()
p1.size = 100
p2 = Topcoat()
p2.size = -200
print(f" общий расход: {(p1.get_rashod() + p2.get_rashod()):.2f}")

c1 = Costume()
c1.growth = -154
c2 = Costume()
c2.growth = 175
print(f" общий расход: {(c1.get_rashod() + c2.get_rashod()):.2f}")
