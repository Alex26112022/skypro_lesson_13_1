import pytest
from skypro_lesson_13_1.product import Product


def test_product(create_product_book_1):
    """ Проверка инициализации класса Product. """
    assert create_product_book_1.name == 'Война и мир'
    assert create_product_book_1.description == 'Художественный роман'
    assert create_product_book_1.price == 2150.23
    assert create_product_book_1.quantity == 15


def test_create_product():
    """ Проверка класс-метода создания объекта Product. """
    new_product = Product.create_product('Автомир',
                                         'Журнал для автолюбителей',
                                         500.00, 37)
    assert type(new_product) is Product
    assert new_product.name == 'Автомир'
    assert new_product.description == 'Журнал для автолюбителей'
    assert new_product.price == 500.00
    assert new_product.quantity == 37
