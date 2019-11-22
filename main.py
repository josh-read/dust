from random import random
from math import sqrt, pi

G = 1
DENSITY = 1


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x:.2f}, {self.y:.2f})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


class Geometry:

    @staticmethod
    def scalar_dist(p1: Vector, p2: Vector) -> float:
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        return sqrt(pow(dx, 2) + pow(dy, 2))

    @staticmethod
    def collision(r1: float, p1: Vector, r2: float, p2: Vector) -> bool:
        critical_distance = r1 + r2
        if Geometry.scalar_dist(p1, p2) < critical_distance:
            return True
        else:
            return False

    @staticmethod
    def radius_from_mass(mass: float) -> float:
        return sqrt(mass/(pi * DENSITY))


class Particle:

    def __init__(self, mass, position):
        self.mass = mass
        self.position = position
        self.radius = Geometry.radius_from_mass(mass)
        self.momentum = 0

    def two_body_force(self, other):
        pass

    def net_force(self, dust: dict) -> Vector:
        f_net = 0
        for particle in dust:
            f_net += self.two_body_force(particle)
        return f_net

    @classmethod
    def random(cls):
        mass = random(0, 10)
        position = (random(-5, 5), random(-5, 5))
        return cls(mass, position)
