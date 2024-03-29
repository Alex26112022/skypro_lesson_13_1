from abc import ABC, abstractmethod


class AbcProduct:
    """ Абстракция класса продукты. """
    @abstractmethod
    def create_product(self):
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
