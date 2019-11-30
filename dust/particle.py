import random
from math import isclose, pi, sqrt

from dust.vector import Vector


class Particle:

    def __init__(self, mass, position, momentum=Vector(0, 0), rho=0.2):
        self._mass = mass
        self.position = position
        self.momentum = momentum
        self.velocity = momentum / mass
        self.rho = rho
        try:
            self.radius = self.radius_from_mass()
        except ValueError:  # Raised when negative mass is used
            self.radius = 0

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        self._mass = mass
        try:
            self.radius = self.radius_from_mass()
        except ValueError:  # Raised when negative mass is used
            self.radius = 0

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
        if type(other) == int:
            other = Particle(0, Vector(0, 0))
        mass = self.mass + other.mass
        position = self.centre_of_mass(other)
        momentum = self.momentum + other.momentum
        return Particle(mass, position, momentum)

    __radd__ = __add__

    def __neg__(self):
        return Particle(-self.mass, self.position, -self.momentum)

    def __sub__(self, other):
        return self + (- other)

    def __mod__(self, other) -> bool:
        return self.check_collision(other)

    def radius_from_mass(self) -> float:
        return sqrt(self.mass/(pi * self.rho))

    def centre_of_mass(self, other) -> Vector:
        return (self.mass * self.position + other.mass * other.position) \
                / (abs(self.mass) + abs(other.mass))

    def two_body_force(self, other, g) -> Vector:
        m1 = self.mass
        m2 = other.mass
        r1 = self.position
        r2 = other.position
        r = r2.scalar_dist(r1)
        u = (r2-r1).unit_vector()
        try:
            return ((g * m1 * m2) / r**2) * u
        except ZeroDivisionError:
            return Vector(0, 0)

    def net_force(self, dust: list, g: float) -> Vector:
        f_net = Vector(0, 0)
        for particle in dust:
            f_net += self.two_body_force(particle, g)
        return f_net

    @staticmethod
    def quick_force(particles: list) -> list:
        """Takes a list of particles and reutrns a list of vectors
        representing the net force on each particle."""
        n = len(particles)
        forces = [Vector(0, 0) for _ in range(n)]
        # when multithreading split on the first range of for loop
        for i in range(0, n):
            for j in range(i+1, n):
                f = particles[i].two_body_force(particles[j], 0.1)
                forces[i] += (f)
                forces[j] += (-f)
        return forces

    def two_body_amomentum(self, other) -> float:
        """Returns the angular momentum of particle relative to other.
        L = r x p."""
        r = other.position - self.position
        p = other.momentum - self.momentum
        return Vector.cross(r, p)

    def net_amomentum(self, dust: list) -> float:
        l_net = 0
        for particle in dust:
            l_net += self.two_body_amomentum(particle)
        return l_net

    def check_collision(self, other) -> bool:
        critical_distance = self.radius + other.radius
        particle_seperation = self.position.scalar_dist(other.position)
        if particle_seperation <= critical_distance:
            return True
        else:
            return False

    def update(self, dust: list, dt: float, g: float):
        self.momentum += dt * self.net_force(dust, g)
        self.velocity = self.momentum / self.mass
        self.position += dt * self.velocity

    @classmethod
    def random_static(cls, rho):
        mass = random.randint(1, 10)
        position = Vector(random.randint(0, 800), random.randint(0, 500))
        return cls(mass, position, rho=rho)
