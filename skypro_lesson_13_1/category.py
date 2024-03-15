from skypro_lesson_13_1.product import Product


class Category:
    """ Описывает категории. """
    name: str
    description: str
    __products: list
    count_name: int
    count_products: int

    count_name = 0  # Счетчик категорий.
    count_products = 0  # Счетчик уникальных товаров.

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.count_name += 1
        Category.count_products += len(self.__products)

    def add_products(self, name, description, price, quantity):
        """ Добавляет товар. """
        self.__products.append(Product(name, description, price, quantity))

    def _get_products(self):
        """ Возвращает список товаров. """
        return self.__products

    @property
    def prod(self):
        """ Выводит данные о продуктах категории в заданном формате. """
        for el in self.__products:
            print(f'{el.name}, {el.price} руб. Остаток: {el.quantity} шт.')
        return self.__products
