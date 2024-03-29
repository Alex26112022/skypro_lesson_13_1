from skypro_lesson_13_1.mixin_log import MixinLog
from skypro_lesson_13_1.product import Product


class Smartphone(Product, MixinLog):
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
        MixinLog.__init__(self, name, description, price_, quantity, color,
                          performance, model, memory)
        self.performance = performance
        self.model = model
        self.memory = memory
