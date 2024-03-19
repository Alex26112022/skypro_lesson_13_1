import pytest

from skypro_lesson_13_1.iter_category import IterCategory


def test_iter_category(create_category_toy):
    """ Проверяет итерирование по товарам категории.  """
    iter_object = IterCategory(create_category_toy)
    iter_list = []
    for el in iter_object:
        print(el)
        iter_list.append(el)
    assert len(iter_list) == 3
