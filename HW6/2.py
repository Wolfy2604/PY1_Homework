class Road:

    _sm_1_weight = 25

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness

    def calc_weight(self):
        result = self._length * self._width * self._thickness * self._sm_1_weight
        return result


name_road = Road(2000, 4, 5)
print(name_road.calc_weight())