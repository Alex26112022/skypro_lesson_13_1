from skypro_lesson_13_1.lawn_grass import LawnGrass
from skypro_lesson_13_1.product import Product
from skypro_lesson_13_1.smartphone import Smartphone


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
        if isinstance(products, list) and len(products) == 0:
            self.__products = products
        elif isinstance(products, list) and len(products) > 0 and all(map(lambda x: isinstance(x, Product), products)):
            self.__products = products
        else:
            raise TypeError('products может быть списком с объектами класса'
                            'Product и его наследниками!!!')
        Category.count_name += 1
        Category.count_products += len(self.__products)

    def add_products(self, name, description, price, quantity):
        """ Добавляет товар. """
        new_product = Product.create_product(name, description, price,
                                             quantity)
        for el in self.__products:
            if new_product.name.lower() == el.name.lower():
                el.quantity += new_product.quantity
                el.price = max(el.price, new_product.price)
                return
        self.__products.append(new_product)
        Category.count_products += 1

    def _get_products(self):
        """ Возвращает список товаров. """
        return self.__products

    @property
    def prod(self):
        """ Выводит данные о продуктах категории в заданном формате. """
        info_str = []
        for el in self.__products:
            info_str.append(f'{el.name}, {el.price} руб. Остаток:'
                            f' {el.quantity} шт.\n')
        return info_str

    def __len__(self):
        """
        Возвращает общее количество товаров заданной категории на складе.
        """
        all_products = 0
        for el in self.__products:
            all_products += el.quantity
        return all_products

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'
