from skypro_lesson_13_1.category import Category
from skypro_lesson_13_1.lawn_grass import LawnGrass
from skypro_lesson_13_1.order_abc import OrderAbc
from skypro_lesson_13_1.product import Product
from skypro_lesson_13_1.smartphone import Smartphone


class Order(OrderAbc):
    """ Класс покупок. """
    def __init__(self, name_category: Category, name_product, amount):
        self.name_category = name_category
        self.name_product = name_product
        self.amount = amount
        self.product = None
        self.real_price = '?'
        self.real_quantity = '?'
        if bool(self.name_category.get_products()):
            for el in self.name_category.get_products():
                if el.name.lower() == self.name_product.lower():
                    self.product = el
        else:
            print('Список товаров пуст!')

    def get_total_price(self):
        """ Возвращает итоговую стоимость. """
        if self.product is not None:
            self.real_price = self.product.price
            self.real_quantity = self.product.quantity
            if self.amount <= self.product.quantity:
                return self.amount * self.real_price
            else:
                return 'Нет такого количества требуемого товара!'

        else:
            return 'Нет такого товара!'

    def __repr__(self):
        info_price = self.get_total_price()
        return (
            f'Товар: {self.name_product}, Цена: {self.real_price}, '
            f'На складе: {self.real_quantity}, '
            f'Требуемое количество: {self.amount},'
            f' Итог: {info_price}')
