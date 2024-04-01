from skypro_lesson_13_1.lawn_grass import LawnGrass
from skypro_lesson_13_1.mixin_log import MixinLog
from skypro_lesson_13_1.my_exception import MyException
from skypro_lesson_13_1.order_abc import OrderAbc
from skypro_lesson_13_1.product import Product
from skypro_lesson_13_1.smartphone import Smartphone


class Category(MixinLog, OrderAbc):
    """ Описывает категории. """
    name: str
    description: str
    __products: list
    count_name: int
    count_products: int

    count_name = 0  # Счетчик категорий.
    count_products = 0  # Счетчик уникальных товаров.

    def __init__(self, name, description, products):
        super().__init__(name, description, products)
        self.name = name
        self.description = description
        if isinstance(products, list) and len(products) == 0:
            self.__products = products
        elif isinstance(products, list) and len(products) > 0 and all(
                map(lambda x: isinstance(x, Product), products)):
            self.__products = products
            for el in self.__products:
                if el.quantity == 0:
                    raise ValueError('Товар с нулевым количеством не может '
                                     'быть добавлен!')
        else:
            raise TypeError('products может быть списком с объектами класса'
                            'Product и его наследниками!!!')
        Category.count_name += 1
        Category.count_products += len(self.__products)

    def add_products(self, new_product: Product):
        """ Добавляет товар. """
        try:
            if isinstance(new_product, Product):
                if new_product.quantity == 0:
                    raise MyException()
                    # raise ValueError('Товар с нулевым количеством не может быть добавлен!')
                for el in self.__products:
                    if new_product.name.lower() == el.name.lower():
                        el.quantity += new_product.quantity
                        el.price = max(el.price, new_product.price)
                        return
                self.__products.append(new_product)
                Category.count_products += 1
            else:
                raise TypeError('Добавить можно только объект класса Product и '
                                'его наследников!!!')
        except MyException as ex:
            print(ex)
        else:
            print('Товар добавлен!')
        finally:
            print('Обработка добавления товара завершена!')

    def get_products(self):
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

    def get_medium_price(self):
        """ Возвращает средний ценник всех товаров. """
        sum_of_prices = sum(map(lambda x: x.price, self.__products))
        try:
            medium_price = sum_of_prices / len(self.__products)
        except ZeroDivisionError:
            return 0
        return medium_price

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
