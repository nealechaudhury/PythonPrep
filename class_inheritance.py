class Color:
    def __init__(self, _colorpassed):
        self._color = _colorpassed

    @property
    def get_color(self):
        return (self._color)

    @get_color.setter
    def get_color(self, _newcolor):
        self._color = _newcolor


class Shape (Color):
    def __init__ (self, color, length, width):
        super().__init__(color)
        self._length = length
        self._width = width

    def area(self):
        return (self._width * self._length)

    def perimeter(self):
        return (2*self._length * self._width)
