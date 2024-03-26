import pytest
from skypro_lesson_13_1.category import Category
from skypro_lesson_13_1.product import Product


def test_count_category(create_category_book, create_category_toy):
    """ Проверяет счетчики категорий и товаров. """
    category1 = create_category_book
    category2 = create_category_toy
    assert category1.count_name == 2
    assert category1.count_products == 5
    category2.add_products('тетрис', 'карманное электронное устройство',
                           4500.70, 20)
    assert category1.count_name == 2
    assert category2.count_name == 2
    assert category1.count_products == 6


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
    create_category_book.add_products('Из рук в руки', 'Газета',
                                      400.00, 15)
    assert len(create_category_book._get_products()) == 3
    assert create_category_book._get_products()[2].price == 400.00
    assert create_category_book._get_products()[2].quantity == 230


def test_prod(create_category_toy):
    """ Тестирует вывод информации. """
    assert create_category_toy.prod == ['мяч, 5000.4 руб. Остаток: 42 шт.\n',
                                        'шахматы, 2100.0 руб. Остаток: 14 '
                                        'шт.\n',
                                        'Xbox, 40000.0 руб. Остаток: 5 шт.\n']


def test_add_create_product(create_category_book):
    """ Проверка добавления объекта через класс-метод класса Product. """
    assert len(create_category_book._get_products()) == 2
    create_category_book.add_products('Автомир', 'Журнал для автолюбителей',
                                      500.00, 37)
    assert len(create_category_book._get_products()) == 3
    assert type(create_category_book._get_products()[2]) == Product
    assert create_category_book._get_products()[
               2].description == 'Журнал для автолюбителей'
    create_category_book.add_products('Автомир', 'Журнал для автолюбителей',
                                      400.00, 3)
    assert len(create_category_book._get_products()) == 3
    assert create_category_book._get_products()[2].price == 500.00
    assert create_category_book._get_products()[2].quantity == 40
    create_category_book.add_products('Автомир', 'Журнал для автолюбителей',
                                      600.00, 10)
    assert len(create_category_book._get_products()) == 3
    assert create_category_book._get_products()[2].price == 600.00
    assert create_category_book._get_products()[2].quantity == 50


def test_len(create_category_toy):
    """ Проверяет общее количество товаров на складе для заданной категории. """
    assert len(create_category_toy) == 61


def test_str(create_category_toy):
    print(create_category_toy)


def test_len_smartphone(create_category_smartphone):
    """ Проверяет общее количество товаров на складе для категории смартфон. """
    assert len(create_category_smartphone) == 260


def test_len_lawn_grass(create_category_grass):
    """
    Проверяет общее количество товаров на складе для категории трава газонная.
    """
    assert len(create_category_grass) == 55
