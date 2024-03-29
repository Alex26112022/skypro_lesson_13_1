import pytest

from config import products_json_test
from skypro_lesson_13_1.category import Category
from skypro_lesson_13_1.generate_products import load_json, generate_products
from skypro_lesson_13_1.product import Product


def test_load_json():
    """ Тест загрузки json """
    assert len(load_json(products_json_test)) == 2
    assert type(load_json(products_json_test)) == list
    assert load_json(products_json_test)[0]["name"] == "Смартфоны"


def test_generate_products():
    """ Тест генератора объектов классов. """
    assert type(generate_products(products_json_test)) == list
    assert len(generate_products(products_json_test)) == 2
    assert type(generate_products(products_json_test)[0]) == Category
    assert type(generate_products(products_json_test)[1]) == Category
    assert generate_products(products_json_test)[0].name == 'Смартфоны'
    assert (generate_products(products_json_test)[0].get_products()[0].name
            == 'Samsung Galaxy C23 Ultra')
