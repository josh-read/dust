class Vector:

    def __init__(self, x: float, y: float):

        if type(x) == int or type(x) == float:
            self.x = x
        else:
            raise TypeError("x must be either a float or integer")

        if type(y) == int or type(y) == float:
            self.y = y
        else:
            raise TypeError("x must be either a float or integer")

    def __repr__(self):
        return f"Vector({self.x:.2f}, {self.y:.2f})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        """Multiplication is only defined as a scalar multiplication."""
        if type(other) == int or type(other) == float:
            return Vector(other * self.x, other * self.y)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and "
                            + type(other).__name__)

    __rmul__ = __mul__

    def __truediv__(self, other):
        """Division is only defined as a scalar division."""
        if type(other) == int or type(other) == float:
            return Vector(self.x / other, self.y / other)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Vector' and "
                            + type(other).__name__)

