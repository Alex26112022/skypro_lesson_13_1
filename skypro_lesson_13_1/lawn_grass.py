from skypro_lesson_13_1.mixin_log import MixinLog
from skypro_lesson_13_1.product import Product


class LawnGrass(Product, MixinLog):
    """ Описывает товар Трава газонная. """
    name: str
    description: str
    __price: float
    quantity: int
    color: str

    manufacturer_country: str
    germination_period: float

    def __init__(self, name, description, price, quantity, color,
                 manufacturer_country, germination_period):
        super().__init__(name, description, price, quantity, color)
        MixinLog.__init__(self, name, description, price, quantity, color,
                          manufacturer_country, germination_period)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
