import json

from config import products_json
from skypro_lesson_13_1.product import Product
from skypro_lesson_13_1.category import Category


def load_json(json_path):
    """ Загружает данные товаров из файла-json. """
    with open(json_path, 'r', encoding='utf-8') as f:
        file = f.read()
        file = json.loads(file)
    return file


def generate_products(json_path):
    """ Генерирует объекты классов. """
    category_list = []
    products_list = []
    for el in load_json(json_path):
        category_list.append(Category(el['name'], el['description'],
                                      list(map(lambda x: x["name"],
                                               el['products']))))

        for item in el['products']:
            products_list.append(Product(item['name'], item['description'],
                                         item['price'], item['quantity']))

    return category_list, products_list


if __name__ == '__main__':
    generate_products(products_json)
