#!/usr/local/bin/python3

class Vehicle(object):

    def __init__(self, max_speed):
        self._max_speed = max_speed

    def max_speed(self):
        return self._max_speed


class Car(Vehicle):

    def __init__(self):
        super().__init__(120)
        self._number_of_doors = 4

    @property
    def number_of_doors(self):
        return self._number_of_doors



class Boat(Vehicle):

    def __init__(self):
        super().__init__(20)





a = Car()
b = Boat()
print(a.max_speed())
print(b.max_speed())

# print(a.number_of_doors)
# print(b.number_of_doors)

my_vehicles = [a, b]
print(', '.join([str(ve.max_speed()) for ve in my_vehicles if isinstance(ve, Vehicle)]))


# c = "car fake object"
# my_vehicles = [a, b, c]
# print(', '.join([str(ve.max_speed()) for ve in my_vehicles if isinstance(ve, Vehicle)]))
#
#
#
# c = "car fake object"
# my_vehicles = [a,b]
# print(([ve.number_of_doors for ve in my_vehicles ])

print(issubclass(Car, Vehicle))