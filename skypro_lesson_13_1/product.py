class Product:
    """ Описывает товары. """
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price_, quantity):
        self.name = name
        self.description = description
        self.__price = price_
        self.quantity = quantity

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
