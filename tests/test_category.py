import pytest
from skypro_lesson_13_1.category import Category


@pytest.fixture()
def create_category_1():
    return Category('Книги', 'Печатная продукция',
                    ['Война и мир', 'Вий', 'Мастер и Маргарита'])


@pytest.fixture()
def create_category_2():
    return Category('Игрушки', 'Товары для детей',
                    ['машинка', 'вертолет', 'мяч', 'пистолет'])


@pytest.fixture()
def create_category_3():
    return Category('Настольные игры', 'Развлечения для компании',
                    ['Покер', 'Мафия'])


def test_count_category(create_category_1, create_category_2,
                        create_category_3):
    category1 = create_category_1
    category2 = create_category_2
    category3 = create_category_3
    assert category1.count_name == 3
    assert category1.count_products == 9


def test_init_category(create_category_1):
    assert create_category_1.name == 'Книги'
    assert create_category_1.description == 'Печатная продукция'
    assert create_category_1.products == ['Война и мир', 'Вий', 'Мастер и '
                                                                'Маргарита']
