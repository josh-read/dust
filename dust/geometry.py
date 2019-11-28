from math import pi, sqrt

from dust.vector import Vector


def scalar_dist(p1: Vector, p2: Vector) -> float:
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return sqrt(pow(dx, 2) + pow(dy, 2))


def unit_vector(v: Vector) -> Vector:
    return v / scalar_dist(Vector(0, 0), v)


def check_collision(r1: float, p1: Vector, r2: float, p2: Vector) -> bool:
    critical_distance = r1 + r2
    if scalar_dist(p1, p2) <= critical_distance:
        return True
    else:
        return False
