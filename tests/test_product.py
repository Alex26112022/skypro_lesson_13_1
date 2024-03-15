import pytest
from skypro_lesson_13_1.product import Product


def test_product(create_product_book_1):
    """ Проверка инициализации класса Product. """
    assert create_product_book_1.name == 'Война и мир'
    assert create_product_book_1.description == 'Художественный роман'
    assert create_product_book_1.price_ == 2150.23
    assert create_product_book_1.quantity == 15
    assert create_product_book_1.__dict__ == {'_Product__price': 2150.23,
                                              'description': 'Художественный роман',
                                              'name': 'Война и мир',
                                              'quantity': 15}
    del create_product_book_1.price_
    assert create_product_book_1.__dict__ == {'description': 'Художественный роман',
                                              'name': 'Война и мир',
                                              'quantity': 15}


def test_create_product():
    """ Проверка класс-метода создания объекта Product. """
    new_product = Product.create_product('Автомир',
                                         'Журнал для автолюбителей',
                                         0, 37)
    assert type(new_product) is Product
    assert new_product.name == 'Автомир'
    assert new_product.description == 'Журнал для автолюбителей'
    assert new_product.price_ == 0
    assert new_product.quantity == 37
    new_product.price_ = 5
    assert new_product.price_ == 5
