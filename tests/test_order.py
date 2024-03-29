import pytest

from skypro_lesson_13_1.category import Category
from skypro_lesson_13_1.order import Order


def test_order(create_category_smartphone):
    """ Тестирует класс покупок. """
    new_order = Order(create_category_smartphone, 'iphone', 5)
    assert repr(new_order) == ('Товар: iphone, Цена: 100000, На складе: 20, '
                               'Требуемое количество: 5, Итог: 500000')
    new_order = Order(create_category_smartphone, 'iphone', 30)
    assert repr(new_order) == ('Товар: iphone, Цена: 100000, На складе: 20, '
                               'Требуемое количество: 30, Итог: Нет такого '
                               'количества требуемого товара!')
    new_order = Order(create_category_smartphone, 'шляпа', 8)
    assert repr(new_order) == ('Товар: шляпа, Цена: ?, На складе: ?, '
                               'Требуемое количество: 8, Итог: Нет такого '
                               'товара!')
    new_cat = Category('test', 'test description', [])
    new_order = Order(new_cat, 'samsung', 3)
    assert repr(new_order) == ('Товар: samsung, Цена: ?, На складе: ?, '
                               'Требуемое количество: 3, Итог: Нет такого '
                               'товара!')
