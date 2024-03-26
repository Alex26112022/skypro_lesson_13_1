import pytest
from skypro_lesson_13_1.smartphone import Smartphone


def test_smartphone(create_smartphone_1):
    """ Проверка класса Smartphone. """
    assert create_smartphone_1.__dict__ == {'_Product__price': 100000,
                                            'color': 'gold',
                                            'description': 'Смартфон для мажоров',
                                            'name': 'IPhone',
                                            'quantity': 20,
                                            'memory': 1024,
                                            'model': '15ProMax',
                                            'performance': 1641883, }
    create_smartphone_1.price = 120000
    assert create_smartphone_1.price == 120000
    del create_smartphone_1.price
    assert create_smartphone_1.__dict__ == {'color': 'gold',
                                            'description': 'Смартфон для мажоров',
                                            'name': 'IPhone',
                                            'quantity': 20,
                                            'memory': 1024,
                                            'model': '15ProMax',
                                            'performance': 1641883, }
