import pytest

from dust.vector import Vector
import dust.geometry as geo


A = Vector(0, 0)
B = Vector(5, 0)
C = Vector(-3.14, 0)
D = Vector(3, 4)


class TestGeometry:

    def test_scalar_dist(self):
        assert geo.scalar_dist(A, B) == 5
        assert geo.scalar_dist(A, C) == 3.14
        assert geo.scalar_dist(A, D) == 5

    def test_unit_vector(self):
        assert geo.unit_vector(A) == Vector(0, 0)
        assert geo.unit_vector(B) == Vector(1, 0)
        assert geo.unit_vector(C) == Vector(-1, 0)
        assert geo.unit_vector(D) == Vector(3/5, 4/5)

    def test_collision(self):
        assert geo.check_collision(3, A, 3, B)
        assert geo.check_collision(2.5, A, 2.5, B)
        assert not geo.check_collision(2, A, 2, B)
