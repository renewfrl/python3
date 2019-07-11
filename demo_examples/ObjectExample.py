
#!/usr/local/bin/python3
class Human(object):

    name = "Human"

    def __init__(self, a, c):
        self.city = c
        self.age = a
        print("----")
        print("create human with age {} and city {}".format(a,c))

    def is_adult(self):
        return self.age >= 18


    def lives_in_metropole(self):
        return self.city == 'newyork'

    def tell_me(self):
        print("human {} adult: {} and lives in metropole {}".format(Human.name,  self.is_adult(), self.lives_in_metropole()))


human1 = Human(23,'leewuarden')
human1.tell_me()
human2 = Human(10,'newyork')
human2.tell_me()

#however

# print(human1.age)
# print(human1.city)


