from abc import ABC, abstractmethod


class AbcProduct:
    """ Абстракция класса продукты. """

    @classmethod
    @abstractmethod
    def create_product(cls, name, description, price, quantity):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
