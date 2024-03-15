class Product:
    """ Описывает товары. """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """ Создает и возвращает объект Product. """
        return cls(name, description, price, quantity)

    @property
    def price_(self):
        """ Возвращает цену. """
        if self.__price == 0:
            print('Цена введена некорректная!')
        return self.__price

    @price_.setter
    def price_(self, price):
        """ Изменяет цену. """
        self.__price = price
