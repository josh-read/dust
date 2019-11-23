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


if __name__ == '__main__':
    testing.main()
