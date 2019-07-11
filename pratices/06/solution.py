class Airplane(object):

    def __init__(self, current_f):
        self.__max_range = 1000
        self.__current_fuel = None
        self.current_fuel = current_f

    @property
    def current_fuel(self):
        return self.__current_fuel

    @current_fuel.setter
    def current_fuel(self, x):
        if x < 10:
            raise Exception("not enough fuel")
        self.__current_fuel = x

    @property
    def max_range(self):
        return self.__max_range

    def move(self):
        self.current_fuel -= 1



a = Airplane(100)

print(a.current_fuel)
print(a.max_range)
a.move()
print(a.current_fuel)
