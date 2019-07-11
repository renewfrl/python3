class Airplane(object):

    def __init__(self, max_range):
        self._max_range = max_range
        self._distance = 0

    @property
    def range(self):
        return self._max_range


class FighterJet(Airplane):

    def __init__(self):
        super().__init__(1000)


class CommercialJet(Airplane):

    def __init__(self):
        super().__init__(5000)





a = FighterJet()
b = CommercialJet()
print(a.range)
print(b.range)

