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

    def __add__(self, other):
        mass = self.mass + other.mass
        position = self.centre_of_mass(self, other)
        momentum = self.momentum + other.momentum
        return Particle(mass, position, momentum)

    def __mod__(self, other) -> bool:
        return geo.check_collision(self.radius, self.position,
                                   other.radius, other.position)

    def centre_of_mass(self, other):
        return (self.mass * self.position + other.mass * other.position) \
                / (self.mass + other.mass)

    def two_body_force(self, other):
        dist_x = (other.position.x - self.position.x)
        dist_y = (other.position.y - self.position.y)

        try:
            F_x = G * self.mass * other.mass / pow(dist_x, 2)
        except ZeroDivisionError:
            F_x = 0

        try:
            F_y = G * self.mass * other.mass / pow(dist_y, 2)
        except ZeroDivisionError:
            F_y = 0

        return Vector(F_x, F_y)

    def net_force(self, dust: list) -> Vector:
        f_net = Vector(0, 0)
        for particle in dust:
            f_net += self.two_body_force(particle)
        return f_net

    def update(self, dust: list, dt: float):
        self.momentum += dt * self.net_force(dust)
        self.velocity = self.momentum / self.mass
        self.position += dt * self.velocity

    @classmethod
    def random(cls):
        mass = random.randint(1, 10)
        position = Vector(random.randint(0, 800), random.randint(0, 500))
        return cls(mass, position)