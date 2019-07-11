class Airplane(object):

    def __init__(self, max_range):
        self._max_range = max_range
        self._distance = 0

    def print_max_range(self):
        print(self._max_range)

    def move(self, step=20):
        self._distance += step

    def is_out_of_range(self):
        return self._distance > self._max_range



a = Airplane(100)

a.move()
a.move(50)
print(a._distance)