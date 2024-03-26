import pytest
from skypro_lesson_13_1.lawn_grass import LawnGrass


def test_lawn_grass(create_lawn_glass_1):
    """ Проверка класса LawnGrass. """
    assert create_lawn_glass_1.__dict__ == {'_Product__price': 10000,
                                            'color': 'green',
                                            'description': 'для гольфа',
                                            'name': 'Трава обычная',
                                            'quantity': 15,
                                            'manufacturer_country': 'England',
                                            'germination_period': 360}
    create_lawn_glass_1.price = 15000
    assert create_lawn_glass_1.price == 15000
    del create_lawn_glass_1.price
    assert create_lawn_glass_1.__dict__ == {'color': 'green',
                                            'description': 'для гольфа',
                                            'name': 'Трава обычная',
                                            'quantity': 15,
                                            'manufacturer_country': 'England',
                                            'germination_period': 360}
