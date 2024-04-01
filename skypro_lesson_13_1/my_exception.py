class MyException(Exception):
    """
    Класс исключения, который отвечает за обработку событий, когда в
    «Категорию» или в «Заказ» добавляется товар с нулевым количеством.
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ('Количество товаров не должно '
                                             'быть нулевым!')

    def __str__(self):
        return self.message
