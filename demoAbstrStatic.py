from abc import ABC, abstractmethod
import random


class Animal(ABC):

    @abstractmethod
    def crier(self):
        pass

    @property
    @abstractmethod
    def nom(self):
        pass


class Chat(Animal):

    def __init__(self, nom):
        self._nom = nom

    def crier(self):
        print("Miaou")

    @property
    def nom(self):
        return self._nom


class Constante:
    PI = 3.14


class De:
    @staticmethod
    def De6():
        return random.randint(1, 6)


print(Constante.PI)
print(De.De6())
