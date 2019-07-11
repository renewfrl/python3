#!/usr/local/bin/python3

class Vehicle(object):


    def name(self):
        return "unknown"


class Car(Vehicle):


    def name(self):
        return "car"



class Boat(Vehicle):

    def name(self):
        return "boaty"




a = Vehicle()
b = Car()
c = Boat()
veh = [a,b,c]
print('\n'.join([v.name() for v in veh]))

# # or good old style
# print("---")
# print(a.name())
# print(b.name())
# print(c.name())