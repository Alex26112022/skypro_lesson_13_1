import pytest

from skypro_lesson_13_1.category import Category
from skypro_lesson_13_1.product import Product


@pytest.fixture()
def create_product_book_1():
    """ Создает объект класса Product. """
    return Product('Война и мир', 'Художественный роман', 2150.23, 15)


@pytest.fixture()
def create_product_book_2():
    """ Создает объект класса Product. """
    return Product('Советская энциклопедия', 'Научно-популярная литература',
                   3000.50,
                   4)


@pytest.fixture()
def create_product_toy_1():
    """ Создает объект класса Product. """
    return Product('мяч', 'спорт-инвентарь', 5000.40, 42)


@pytest.fixture()
def create_product_toy_2():
    """ Создает объект класса Product. """
    return Product('шахматы', 'настольные игры', 2100.00, 14)


@pytest.fixture()
def create_product_toy_3():
    """ Создает объект класса Product. """
    return Product('Xbox', 'электроника', 40000.00, 5)


@pytest.fixture()
def create_category_book(create_product_book_1, create_product_book_2):
    """ Создает экземпляр 1 класса Category. """
    return Category('Книги', 'Печатная продукция',
                    [create_product_book_1, create_product_book_2])


@pytest.fixture()
def create_category_toy(create_product_toy_1, create_product_toy_2,
                        create_product_toy_3):
    """ Создает экземпляр 2 класса Category. """
    return Category('Игрушки', 'Сфера развлечений',
                    [create_product_toy_1, create_product_toy_2,
                     create_product_toy_3])
