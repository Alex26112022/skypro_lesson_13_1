class Product:
    """ Описывает товары. """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """ Создает и возвращает объект Product. """
        return cls(name, description, price, quantity)
