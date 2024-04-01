import pytest
from skypro_lesson_13_1.category import Category
from skypro_lesson_13_1.lawn_grass import LawnGrass
from skypro_lesson_13_1.product import Product
from skypro_lesson_13_1.smartphone import Smartphone
from tests.class_test import ClassTest


def test_count_category(create_category_book, create_category_toy):
    """ Проверяет счетчики категорий и товаров. """
    category1 = create_category_book
    category2 = create_category_toy
    assert category1.count_name == 2
    assert category1.count_products == 5
    category2.add_products(Product('тетрис', 'карманное электронное '
                                             'устройство', 4500.70, 20))
    assert category1.count_name == 2
    assert category2.count_name == 2
    assert category1.count_products == 6


def test_init_category(create_category_toy, create_category_smartphone,
                       create_category_grass):
    """ Проверяет инициализацию класса Category. """
    assert create_category_toy.name == 'Игрушки'
    assert create_category_toy.description == 'Сфера развлечений'
    assert create_category_toy.get_products()[0].name == 'мяч'

    assert create_category_smartphone.name == 'Смартфоны'
    assert create_category_grass.name == 'Трава газонная'
    assert repr(create_category_toy) == (
        "Category('Игрушки', 'Сфера "
        "развлечений', [Product('мяч', 'спорт-инвентарь', 5000.4, 42), "
        "Product('шахматы', 'настольные игры', 2100.0, 14), "
        "Product('Xbox', 'электроника', 40000.0, 5)])")
    assert repr(create_category_grass) == (
        "Category('Трава газонная', 'Товары для дома', [LawnGrass('Трава обычная', "
        "'для гольфа', 10000, 15, 'green', 'England', 360), LawnGrass('Трава "
        "волшебная', 'не подходит для гольфа', 20000, 40, 'yellow', 'Kazakhstan', "
        '200)])')


def test_init_category_error_1():
    """ Проверяет попытку неправильной инициализации категории. """
    with pytest.raises(TypeError):
        assert Category('test_name', 'test_description', 'test_str')


def test_init_category_error_2():
    """ Проверка инициализации при нулевом количестве товара. """
    with pytest.raises(ValueError) as info:
        Category('name', 'description',
                 [Product('name', 'description',
                          2000, 0)])
    assert info.value.args[0] == ('Товар с нулевым количеством не может быть '
                                  'добавлен!')


def test_add_products(create_category_book, create_category_smartphone,
                      create_category_grass):
    """ Проверяет добавление товаров. """
    assert len(create_category_book.get_products()) == 2
    create_category_book.add_products(Product('Из рук в руки', 'Газета',
                                              200.30, 215))
    assert len(create_category_book.get_products()) == 3
    assert type(create_category_book.get_products()[2]) == Product
    assert create_category_book.get_products()[2].description == 'Газета'
    create_category_book.add_products(Product('Из рук в руки', 'Газета',
                                              400.00, 15))
    assert len(create_category_book.get_products()) == 3
    assert create_category_book.get_products()[2].price == 400.00
    assert create_category_book.get_products()[2].quantity == 230
    assert len(create_category_smartphone.get_products()) == 3
    assert str(
        create_category_smartphone) == 'Смартфоны, количество продуктов: 260 шт.'
    create_category_smartphone.add_products(Smartphone(
        'RuPhone', 'Русская версия айфона', 40000,
        10, 'orange', 700, 'NewPro', 1024))
    assert len(create_category_smartphone.get_products()) == 4
    assert str(
        create_category_smartphone) == 'Смартфоны, количество продуктов: 270 шт.'
    assert len(create_category_grass.get_products()) == 2
    assert str(
        create_category_grass) == 'Трава газонная, количество продуктов: 55 шт.'
    create_category_grass.add_products(LawnGrass(
        'Какая-то трава', 'Просто трава', 5000, 40,
        'red', 'USA', 60))
    assert len(create_category_grass.get_products()) == 3
    assert str(
        create_category_grass) == 'Трава газонная, количество продуктов: 95 шт.'


def test_add_product_error_1(create_category_smartphone):
    """ Проверяет попытку добавить посторонний объект. """
    with pytest.raises(TypeError) as type_error:
        create_category_smartphone.add_products(ClassTest(
            'test_name', 'test description', 100, 10
        ))
    assert type_error.value.args[0] == 'Добавить можно только объект класса Product и его наследников!!!'


def test_add_product_error_2(create_category_book):
    """ Проверяет попытку добавить объект с нулевым количеством. """
    with pytest.raises(ValueError) as info:
        create_category_book.add_products(Product('name',
                                                  'description',
                                                  3000, 0))
        assert info.value.args[0] == 'Товар с нулевым количеством не может быть добавлен!'


def test_prod(create_category_toy):
    """ Тестирует вывод информации. """
    assert create_category_toy.prod == ['мяч, 5000.4 руб. Остаток: 42 шт.\n',
                                        'шахматы, 2100.0 руб. Остаток: 14 '
                                        'шт.\n',
                                        'Xbox, 40000.0 руб. Остаток: 5 шт.\n']


def test_add_create_product(create_category_book):
    """ Проверка добавления объекта через класс-метод класса Product. """
    assert len(create_category_book.get_products()) == 2
    create_category_book.add_products(Product('Автомир', 'Журнал для '
                                                         'автолюбителей',
                                              500.00, 37))
    assert len(create_category_book.get_products()) == 3
    assert type(create_category_book.get_products()[2]) == Product
    assert create_category_book.get_products()[
               2].description == 'Журнал для автолюбителей'
    create_category_book.add_products(Product('Автомир', 'Журнал для '
                                                         'автолюбителей',
                                              400.00, 3))
    assert len(create_category_book.get_products()) == 3
    assert create_category_book.get_products()[2].price == 500.00
    assert create_category_book.get_products()[2].quantity == 40
    create_category_book.add_products(Product('Автомир', 'Журнал для '
                                                         'автолюбителей',
                                              600.00, 10))
    assert len(create_category_book.get_products()) == 3
    assert create_category_book.get_products()[2].price == 600.00
    assert create_category_book.get_products()[2].quantity == 50


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


def test_get_medium_price(create_category_book):
    """ Проверяет метод, возвращающий средний ценник всех товаров. """
    assert create_category_book.get_medium_price() == 2575.365
    new_cat = Category('name', 'description', [])
    assert new_cat.get_medium_price() == 0
