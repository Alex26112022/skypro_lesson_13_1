from skypro_lesson_13_1.abc_product import AbcProduct


class Product(AbcProduct):
    """ Описывает товары. """
    name: str
    description: str
    __price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color=None):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """ Создает и возвращает объект Product. """
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Возвращает цену. """
        if self.__price == 0:
            print('Цена введена некорректная!')
        return self.__price

    @price.setter
    def price(self, price_):
        """ Изменяет цену. """
        if price_ < self.__price:
            user_input = input('Подтвердите понижение цены: [y/n] ')
            if user_input.lower() == 'y':
                self.__price = price_
        else:
            self.__price = price_

    @price.deleter
    def price(self):
        """ Удаляет аттрибут цена """
        del self.__price

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """
        Возвращает общую стоимость суммированных товаров с учетом их
        количества на складе.
        """
        if type(self) is type(other):
            return (self.__price * self.quantity) + (other.__price *
                                                     other.quantity)
        raise TypeError('Товары принадлежат разным классам!')
