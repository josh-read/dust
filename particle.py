import random

from vector import Vector
import geometry as geo

G = 0.1


class Particle:

    def __init__(self, mass, position, momentum=Vector(0, 0)):
        self.mass = mass
        self.position = position
        self.radius = geo.radius_from_mass(mass)
        self.momentum = momentum
        self.velocity = momentum / mass

    def __repr__(self):
        return f"Particle({self.mass}, {self.position})"

    def __add__(self, other):
        mass = self.mass + other.mass
        position = self.centre_of_mass(other)
        momentum = self.momentum + other.momentum
        return Particle(mass, position, momentum)

    def __mod__(self, other) -> bool:
        return geo.check_collision(self.radius, self.position,
                                   other.radius, other.position)

    def centre_of_mass(self, other) -> Vector:
        return (self.mass * self.position + other.mass * other.position) \
                / (self.mass + other.mass)

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

    def two_body_amomentum(self, other):
        """L = r x p"""
        r = other.position - self.position
        p = other.momentum - self.momentum
        return Vector.cross(r, p)

    def update(self, dust: list, dt: float):
        self.momentum += dt * self.net_force(dust)
        self.velocity = self.momentum / self.mass
        self.position += dt * self.velocity

    @classmethod
    def random_static(cls):
        mass = random.randint(1, 10)
        position = Vector(random.randint(0, 800), random.randint(0, 500))
        return cls(mass, position)
