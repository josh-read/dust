import random
from math import isclose

from dust.vector import Vector
import dust.geometry as geo

G = 0.1


class Particle:

    def __init__(self, mass, position, momentum=Vector(0, 0)):
        self.mass = mass
        self.position = position
        try:
            self.radius = geo.radius_from_mass(mass)
        except ValueError:  # Raised when negative mass is used
            self.radius = 0
        self.momentum = momentum
        self.velocity = momentum / mass

    def __repr__(self):
        return (f"Particle("
                f"Mass({self.mass:.2f}), "
                f"Pos({self.position}), "
                f"Mom({self.momentum}))")

    def __eq__(self, other):
        if (isclose(self.mass, other.mass) and self.position == other.position
                and self.momentum == other.momentum):
            return True
        else:
            return False

    def __add__(self, other):
        mass = self.mass + other.mass
        position = self.centre_of_mass(other)
        momentum = self.momentum + other.momentum
        return Particle(mass, position, momentum)

    def __neg__(self):
        return Particle(-self.mass, self.position, -self.momentum)

    def __sub__(self, other):
        return self + (- other)

    def __mod__(self, other) -> bool:
        return geo.check_collision(self.radius, self.position,
                                   other.radius, other.position)

    def centre_of_mass(self, other) -> Vector:
        return (self.mass * self.position + other.mass * other.position) \
                / (abs(self.mass) + abs(other.mass))

    def two_body_force(self, other) -> Vector:
        m1 = self.mass
        m2 = other.mass
        r1 = self.position
        r2 = other.position
        r = geo.scalar_dist(r2, r1)
        u = geo.unit_vector(r2 - r1)
        try:
            return ((G * m1 * m2) / r**2) * u
        except ZeroDivisionError:
            return Vector(0, 0)

    def net_force(self, dust: list) -> Vector:
        f_net = Vector(0, 0)
        for particle in dust:
            f_net += self.two_body_force(particle)
        return f_net

    def two_body_amomentum(self, other) -> float:
        """L = r x p"""
        r = other.position - self.position
        p = other.momentum - self.momentum
        return Vector.cross(r, p)

    def net_amomentum(self, dust: list) -> float:
        l_net = 0
        for particle in dust:
            l_net += self.two_body_amomentum(particle)
        return l_net

    def update(self, dust: list, dt: float):
        self.momentum += dt * self.net_force(dust)
        self.velocity = self.momentum / self.mass
        self.position += dt * self.velocity

    @classmethod
    def random_static(cls):
        mass = random.randint(1, 10)
        position = Vector(random.randint(0, 800), random.randint(0, 500))
        return cls(mass, position)

    @classmethod
    def static(cls, position_distribution):
        pass

    @classmethod
    def dynamic(cls, position_distribution, momentum_distribution):
        pass
