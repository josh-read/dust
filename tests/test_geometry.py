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
        self.assertEqual(geo.scalar_dist(self.a, self.c), 3.14)
        self.assertEqual(geo.scalar_dist(self.a, self.d), 5)

    def test_unit_vector(self):
        self.assertEqualVector(geo.unit_vector(self.a), Vector(0, 0))
        self.assertEqualVector(geo.unit_vector(self.b), Vector(1, 0))
        self.assertEqualVector(geo.unit_vector(self.c), Vector(-1, 0))
        self.assertEqualVector(geo.unit_vector(self.d), Vector(3/5, 4/5))

    def test_collision(self):
        self.assertTrue(geo.check_collision(3, self.a, 3, self.b))
        self.assertTrue(geo.check_collision(2.5, self.a, 2.5, self.b))
        self.assertFalse(geo.check_collision(2, self.a, 2, self.b))


if __name__ == '__main__':
    testing.main()
