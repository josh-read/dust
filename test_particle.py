import testing

from vector import Vector
from particle import Particle


class TestParticle(testing.TestCase):

    def setUp(self):
        self.a = Particle(1, Vector(0, 0))
        self.b = Particle(1, Vector(0, 10))

    def test_centre_of_mass(self):
        self.assertAlmostEqualVector(
                self.a.centre_of_mass(self.b), Vector(0, 5)
                )

    def test_add(self):
        self.assertAlmostEqualParticle(
                self.a + self.a, Particle(2, Vector(0, 0))
                )

    def test_mod(self):
        pass

    def test_two_body_force(self):
        self.assertAlmostEqualVector(
                self.a.two_body_force(self.b), Vector(0, 1/100)
                )
        self.assertAlmostEqualVector(
                self.b.two_body_force(self.a), Vector(0, -1/100)
                )


if __name__ == '__main__':
    testing.main()
