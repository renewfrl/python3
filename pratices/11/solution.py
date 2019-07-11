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


class AirLine():

    def __init__(self):
        self.planes = []

    def register(self, plane):
        if isinstance(plane,CommercialJet):
            self.planes.append(plane)

    @property
    def fleet_size(self):
        return len(self.planes)


b = CommercialJet()
b2 = CommercialJet()
b3 = CommercialJet()

a = AirLine()
a.register(b)
a.register(b2)
a.register(b3)

print(a.fleet_size)