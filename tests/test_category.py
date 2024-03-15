import pytest
from skypro_lesson_13_1.category import Category
from skypro_lesson_13_1.product import Product


def test_count_category(create_category_book, create_category_toy):
    """ Проверяет счетчики категорий и товаров. """
    category1 = create_category_book
    category2 = create_category_toy
    assert category1.count_name == 2
    assert category1.count_products == 5


def test_init_category(create_category_toy):
    """ Проверяет инициализацию класса Category. """
    assert create_category_toy.name == 'Игрушки'
    assert create_category_toy.description == 'Сфера развлечений'
    assert create_category_toy._get_products()[0].name == 'мяч'


def test_add_products(create_category_book):
    """ Проверяет добавление товаров. """
    assert len(create_category_book._get_products()) == 2
    create_category_book.add_products('Из рук в руки', 'Газета',
                                      200.30, 215)
    assert len(create_category_book._get_products()) == 3
    assert type(create_category_book._get_products()[2]) == Product
    assert create_category_book._get_products()[2].description == 'Газета'


def test_prod(create_category_toy):
    """ Тестирует вывод информации. """
    assert create_category_toy.prod
