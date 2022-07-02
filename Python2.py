# thickness = 5
# mass = 25


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_road(self, thickness, mass):
        return self._width * self._length * thickness * mass


a = Road(20, 5000)
print(a.mass_road(5, 25))
