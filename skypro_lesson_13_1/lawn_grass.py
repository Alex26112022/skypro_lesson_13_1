from skypro_lesson_13_1.product import Product


class LawnGrass(Product):
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
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
