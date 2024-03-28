import pytest
from skypro_lesson_13_1.product import Product


def test_product(create_product_book_1):
    """ Проверка инициализации класса Product. """
    assert create_product_book_1.name == 'Война и мир'
    assert create_product_book_1.description == 'Художественный роман'
    assert create_product_book_1.price == 2150.23
    assert create_product_book_1.quantity == 15
    assert create_product_book_1.__dict__ == {'_Product__price': 2150.23,
                                              'color': None,
                                              'description': 'Художественный роман',
                                              'name': 'Война и мир',
                                              'quantity': 15}
    del create_product_book_1.price
    assert create_product_book_1.__dict__ == {
        'color': None,
        'description': 'Художественный роман',
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
    assert new_product.price == 0
    assert new_product.quantity == 37
    new_product.price = 5
    assert new_product.price == 5


def test_str(create_product_book_1):
    print(create_product_book_1)


def test_add(create_product_toy_1, create_product_toy_2,
             create_smartphone_1, create_smartphone_2):
    """ Проверяет суммирование стоимости товаров. """
    assert create_product_toy_1 + create_product_toy_2 == 239416.8
    assert create_smartphone_1 + create_smartphone_2 == 4400000


def test_add_error(create_product_book_1, create_smartphone_1,
                   create_lawn_glass_1):
    """ Проверяет невозможность суммирования товаров разных классов. """
    with pytest.raises(TypeError) as type_error:
        create_product_book_1 + create_smartphone_1
        create_product_book_1 + create_lawn_glass_1
        create_smartphone_1 + create_lawn_glass_1

    assert type_error.value.args[0] == 'Товары принадлежат разным классам!'

