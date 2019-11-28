from math import pi, sqrt

from dust.vector import Vector


def scalar_dist(p1: Vector, p2: Vector) -> float:
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return sqrt(pow(dx, 2) + pow(dy, 2))


def unit_vector(v: Vector) -> Vector:
    return v / scalar_dist(Vector(0, 0), v)
