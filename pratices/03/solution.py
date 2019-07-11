class Airplane(object):

    def __init__(self, max_range):
        self._max_range = max_range

    def print_max_range(self):
        print(self._max_range)



a = Airplane(1000)
a.print_max_range()
