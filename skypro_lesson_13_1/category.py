class Category:
    """ Описывает категории. """
    name: str
    description: str
    products: list
    count_name: int
    count_products: int

    count_name = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.count_name += 1
        Category.count_products += len(self.products)
