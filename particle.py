from geometry import Geometry
from vector import Vector
from random import random

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