class Category:
    """ Описывает категории. """
    name: str
    description: str
    __products: list
    count_name: int
    count_products: int

    count_name = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.count_name += 1
        Category.count_products += len(self.__products)

    def add_products(self, product):
        self.__products.append(product)

    def get_products(self):
        return self.__products
