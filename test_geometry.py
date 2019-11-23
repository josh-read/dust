import testing

from vector import Vector
import geometry as geo


class TestGeometry(testing.TestCase):

    def setUp(self):
        self.a = Vector(0, 0)
        self.b = Vector(5, 0)
        self.c = Vector(-3.14, 0)
        self.d = Vector(3, 4)

    def test_scalar_dist(self):
        self.assertEqual(geo.scalar_dist(self.a, self.b), 5)


if __name__ == '__main__':
    testing.main()
