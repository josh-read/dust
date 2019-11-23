from geometry import Geometry
from vector import Vector
from random import random

G = 1


class Particle:

    def __init__(self, mass, position, momentum=0.):
        self.mass = mass
        self.position = position
        self.radius = Geometry.radius_from_mass(mass)
        self.momentum = momentum

    def __add__(self, other):
        mass = self.mass + other.mass
        position = self.centre_of_mass(self, other)
        momentum = self.momentum + other.momentum
        return Particle(mass, position, momentum)

    def centre_of_mass(self, other):
        return (self.mass * self.position + other.mass * other.position) \
                / (self.mass + other.mass)

    def two_body_force(self, other):
        dist_x = (other.position.x - self.position.x)
        dist_y = (other.position.y - self.position.y)

        try:
            F_x = G * self.mass * other.mass / dist_x**2
        except ZeroDivisionError:
            F_x = 0

        try:
            F_y = G * self.mass * other.mass / dist_y**2
        except ZeroDivisionError:
            F_y = 0

        return Vector(F_x, F_y)

    def net_force(self, dust: list) -> Vector:
        f_net = Vector(0, 0)
        for particle in dust:
            f_net += self.two_body_force(particle)
        return f_net

    @classmethod
    def random(cls):
        mass = random(0, 10)
        position = (random(-5, 5), random(-5, 5))
        return cls(mass, position)