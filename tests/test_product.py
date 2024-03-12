import pytest
from skypro_lesson_13_1.product import Product


@pytest.fixture()
def create_product():
    """ Создает объект класса Product. """
    return Product('Война и мир', 'Художественный роман', 2150.23, 15)


def test_product(create_product):
    """ Проверка инициализации класса Product. """
    assert create_product.name == 'Война и мир'
    assert create_product.description == 'Художественный роман'
    assert create_product.price == 2150.23
    assert create_product.quantity == 15
