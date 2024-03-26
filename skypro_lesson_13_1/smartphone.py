from skypro_lesson_13_1.product import Product


class Smartphone(Product):
    """ Описывает товар смартфон. """
    name: str
    description: str
    __price: float
    quantity: int
    color: str

    performance: float
    model: str
    memory: float

    def __init__(self, name, description, price_, quantity, color,
                 performance, model, memory):
        super().__init__(name, description, price_, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory
