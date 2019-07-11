class Airplane(object):

    def __init__(self, max_range, fuel):
        self._max_range = max_range
        self._fuel = fuel

    @property
    def range(self):
        return self._max_range

    @property
    def fuel(self):
        return self._fuel

    def consumption(self):
        pass

    def move(self):
        self._fuel -= self.consumption()



class FighterJet(Airplane):

    def __init__(self):
        super().__init__(1000,50)

    def consumption(self):
        return 5


class CommercialJet(Airplane):

    def __init__(self):
        super().__init__(5000,1000)


    def consumption(self):
        return 1





a = FighterJet()
b = CommercialJet()

a.move()
b.move()

print(a.fuel)
print(b.fuel)
