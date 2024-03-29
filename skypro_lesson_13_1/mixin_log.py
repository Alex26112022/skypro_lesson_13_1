class MixinLog:
    """ Миксин для вывода информации в консоль.  """
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f'{self.__class__.__name__}{self.args}'
