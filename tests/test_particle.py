from dust.vector import Vector
from dust.particle import Particle

A = Particle(1, Vector(0, 0))
B = Particle(1, Vector(0, 10))
C = Particle(3, Vector(5, 2))
D = Particle(1, Vector(0, 0))


class TestParticle:

    def test_centre_of_mass(self):
        assert A.centre_of_mass(B) == Vector(0, 5)

    def test_add(self):
        assert A + B == Particle(2, Vector(0, 5))

    def test_sum(self):
        assert sum([A, B]) == A + B

    def test_sub(self):
        assert (A + B) - B == A

    def test_neg(self):
        assert (-A) == Particle(-1, Vector(0, 0))
        assert (-B) == Particle(-1, Vector(0, 10))
        assert - Particle(2.5, Vector(0.2, 93.5), Vector(34.1, -52.1)) \
            == Particle(-2.5, Vector(0.2, 93.5), Vector(-34.1, 52.1))

    def test_mod(self):
        assert A % A
        assert B % B
        assert not A % B

    def test_two_body_force(self):
        g = 1
        assert A.two_body_force(B, g) == Vector(0, g * 1/100)
        assert B.two_body_force(A, g) == Vector(0, g * -1/100)

    def test_two_body_amomentum(self):
        b = B
        b.momentum = Vector(5, 0)
        assert A.two_body_amomentum(b) == -50
        assert b.two_body_amomentum(A) == -50

    def test_com_force(self):
        """Proof test to check we can't simplify the calculation by
        measuring force from centre of mass rather than summing each
        individual particle."""
        g = 1
        sum_f = A.two_body_force(B, g) + A.two_body_force(C, g)
        com_f = A.two_body_force(B + C, g)
        assert sum_f != com_f
