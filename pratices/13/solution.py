from util.finance import calculate_with_vat

class Airplane(object):

    def __init__(self, max_range, fuel):
        self._max_range = max_range
        self._distance = 0
        self._fuel = fuel

    @property
    def range(self):
        return self._max_range

    @property
    def fuel(self):
        return self._fuel

    @property
    def max_range(self):
        return self._max_range

    def my_registration(self):
        return "I'm flying"

    def consumption(self):
        pass

    def move(self):
        self._fuel -= self.consumption()

    def refuell(self, amount, badge):
        self._fuel += amount


class FighterJet(Airplane):

    def __init__(self):
        super().__init__(1000,50)

    def my_registration(self):
        return "angry plane 002"

    def refuell(self, amount, badge):
        if len(badge) == 4:
            super().refuell(amount,None)


class CommercialJet(Airplane):

    def __init__(self, fuel):
        super().__init__(5000, fuel)

    def my_registration(self):
        return "big plane 001"

    def refuell(self, amount, badge=None):
        pass


    def consumption(self):
        return 1


class AirLine():

    def __init__(self):
        self.planes = []
        self.gas = []

    def register(self, plane):
        if isinstance(plane,CommercialJet):
            self.planes.append(plane)

    def fill_up(self):
        for plane in self.planes:
            amount_needed = plane.max_range-plane.fuel
            self.gas.append(amount_needed)
            plane.refuell(amount_needed,None)

    @property
    def fleet_size(self):
        return len(self.planes)

    def bill(self):
        return calculate_with_vat(self.gas)

b = CommercialJet(100)
b2 = CommercialJet(200)
b3 = CommercialJet(300)

a = AirLine()
a.register(b)
a.register(b2)
a.register(b3)

a.fill_up()
print(a.bill())