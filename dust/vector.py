from math import isclose, sin, cos, sqrt, radians as rad


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

    def __eq__(self, other):
        if isclose(self.x, other.x) and isclose(self.y, other.y):
            return True
        else:
            return False

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __add__(self, other):
        if type(other) == int:
            other = Vector(0, 0)
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    __radd__ = __add__

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
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
            try:
                return Vector(self.x / other, self.y / other)
            except ZeroDivisionError:
                return Vector(0, 0)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Vector' and "
                            + type(other).__name__)

    def scalar_dist(self, other) -> float:
        dx = other.x - self.x
        dy = other.y - self.y
        return sqrt(pow(dx, 2) + pow(dy, 2))

    def unit_vector(self):
        return self / self.scalar_dist(Vector(0, 0))

    @staticmethod
    def cross(v1, v2) -> float:
        return ((v1.x * v2.y) - (v2.x * v1.y))

    def rotate(self, angle: float, radians=False) -> 'Vector':
        """This function takes the angle in degrees."""
        angle = angle if radians else rad(angle)
        x = cos(angle) * self.x - sin(angle) * self.y
        y = sin(angle) * self.x - cos(angle) * self.y
        return Vector(x, y)
