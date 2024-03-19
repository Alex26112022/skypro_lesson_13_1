from skypro_lesson_13_1.category import Category


class IterCategory:
    """
    Принимает на вход категорию и дает возможность использовать цикл for
    для прохода по всем товарам данной категории.
    """
    category: Category

    def __init__(self, category: Category):
        self.category = category

    def __iter__(self):
        self.index_product = -1
        return self

    def __next__(self):
        if self.index_product + 1 < len(self.category._get_products()):
            self.index_product += 1
            return self.category._get_products()[self.index_product]
        else:
            raise StopIteration
