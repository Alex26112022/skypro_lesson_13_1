import pytest

from skypro_lesson_13_1.category import Category
from skypro_lesson_13_1.product import Product
from skypro_lesson_13_1.smartphone import Smartphone
from skypro_lesson_13_1.lawn_grass import LawnGrass


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


@pytest.fixture()
def create_smartphone_1():
    """ Создает объект класса Smartphone. """
    return Smartphone('IPhone', 'Смартфон для мажоров', 100000, 20, 'gold',
                      1641883, '15ProMax', 1024)


@pytest.fixture()
def create_smartphone_2():
    """ Создает объект класса Smartphone. """
    return Smartphone('Samsung', 'Смартфон для нормальных пацанов', 60000,
                      40, 'black',
                      900000, 'Galaxy', 512)


@pytest.fixture()
def create_smartphone_3():
    """ Создает объект класса Smartphone. """
    return Smartphone('Nokia', 'Чисто позвонить', 990,
                      200, 'white',
                      50000, '105 DS', 512)


@pytest.fixture()
def create_lawn_glass_1():
    """ Создает объект класса LawnGrass. """
    return LawnGrass('Трава обычная', 'для гольфа', 10000, 15, 'green',
                     'England', 360)


@pytest.fixture()
def create_lawn_glass_2():
    """ Создает объект класса LawnGrass. """
    return LawnGrass('Трава волшебная', 'не подходит для гольфа', 20000, 40,
                     'yellow',
                     'Kazakhstan', 200)


@pytest.fixture()
def create_category_smartphone(create_smartphone_1, create_smartphone_2,
                               create_smartphone_3):
    """ Создает экземпляр класса Category с товарами категории смартфон. """
    return Category('Смартфоны', 'Товары электроники',
                    [create_smartphone_1,
                     create_smartphone_2,
                     create_smartphone_3])


@pytest.fixture()
def create_category_grass(create_lawn_glass_1, create_lawn_glass_2):
    """
    Создает экземпляр класса Category с товарами категории трава газонная.
    """
    return Category('Трава газонная', 'Товары для дома',
                    [create_lawn_glass_1, create_lawn_glass_2])
