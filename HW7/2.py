import abc

class AbstractWear:

    def __add__(self, other):
        result = self.material_calc + other.material_calc
        return result

    def __getattr__(self, material_calc):
        return float(self.material_calc)

    @abc.abstractmethod
    def material_calc(self):
        pass


class Suit(AbstractWear):

    def __init__(self, height):
        self.height = height

    @property
    def material_calc(self):
        result = 2 * self.height + 0.3
        return result


class Coat(AbstractWear):

    def __init__(self, size):
        self.size = size

    @property
    def material_calc(self):
        result = round((self.size / 6.5 + 0.5), 2)
        return result


def consumption(*args):
    print(args, 'Here')
    return sum(args)


suit1 = Suit(1.8)
coat1 = Coat(45)
print(suit1.material_calc)
print(coat1.material_calc)
print(consumption(suit1.material_calc, coat1.material_calc))


