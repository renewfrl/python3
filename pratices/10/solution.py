class Airplane(object):

    def __init__(self, max_range):
        self._max_range = max_range
        self._distance = 0

    @property
    def range(self):
        return self._max_range

    def my_registration(self):
        return "I'm flying"


class FighterJet(Airplane):

    def __init__(self):
        super().__init__(1000)

    def my_registration(self):
        return "angry plane 002"


class CommercialJet(Airplane):

    def __init__(self):
        super().__init__(5000)

    def my_registration(self):
        return "big plane 001"




a = FighterJet()
b = CommercialJet()
print(a.my_registration())
print(b.my_registration())

