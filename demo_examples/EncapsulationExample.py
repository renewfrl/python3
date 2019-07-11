#!/usr/local/bin/python3


class Human(object):



    def __init__(self, a):
        self.__age = a
        self._name = "rene"
        print("create human with age {}".format(a))

    def is_adult(self):
        return self.__get_age() >= 18

    def __get_age(self):
        if (isinstance(self.__age, int)):
            return self.__age
        else:
            raise Exception("not valid age sorry")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


human1 = Human(23)
print(human1.is_adult())


#print(human1.__get_age())
#print(human1.name)
# print(human1.name)
# print(human1._name)
#print(human1.__age)
# human1 = Human("hahaa")
# print(human1.is_adult())


