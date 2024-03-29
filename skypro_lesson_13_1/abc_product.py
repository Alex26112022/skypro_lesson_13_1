from abc import ABC, abstractmethod


class AbcProduct(ABC):
    """ Абстракция класса продукты. """

    @classmethod
    @abstractmethod
    def create_product(cls):
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
