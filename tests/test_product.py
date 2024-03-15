import pytest
from skypro_lesson_13_1.product import Product


def test_product(create_product_book_1):
    """ Проверка инициализации класса Product. """
    assert create_product_book_1.name == 'Война и мир'
    assert create_product_book_1.description == 'Художественный роман'
    assert create_product_book_1.price == 2150.23
    assert create_product_book_1.quantity == 15
