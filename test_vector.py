import unittest

from vector import Vector


class TestVector(unittest.TestCase):

    def assertEqualVector(self, first, second, msg=None):
        self.assertEqual(first.x, second.x, msg)
        self.assertEqual(first.y, second.y, msg)

    def assertAlmostEqualVector(self, first, second, msg=None):
        self.assertAlmostEqual(first.x, second.x, msg)
        self.assertAlmostEqual(first.y, second.y, msg)

    def setUp(self):
        self.a = Vector(2, 4)
        self.b = Vector(-2.14, -8.23)
        with self.assertRaises(TypeError):
            self.c = Vector('hi', 2 + 3j)

    def test_add(self):
        expected = Vector(-0.14, -4.23)
        self.assertAlmostEqualVector(self.a + self.b, expected)
        sum_ = Vector(0, 0)
        for v in [self.a, self.b]:
            sum_ += v
        self.assertAlmostEqualVector(sum_, expected)

    def test_multiply(self):
        self.assertEqualVector(2 * self.a, Vector(4, 8))
        self.assertEqualVector(self.a * 2, Vector(4, 8))

        self.assertAlmostEqualVector(0.1 * self.b, Vector(-0.214, -0.823))
        self.assertAlmostEqualVector(self.b * 0.1, Vector(-0.214, -0.823))

        with self.assertRaises(TypeError):
            'test' * self.a
        with self.assertRaises(TypeError):
            self.a * ['test']

    def test_divide(self):
        self.assertAlmostEqualVector(self.a / 2, Vector(1, 2))
        self.assertAlmostEqualVector(self.b / 0.1, Vector(-21.4, -82.3))
        with self.assertRaises(TypeError):
            'test' / self.a
        with self.assertRaises(TypeError):
            self.a / ['test']


if __name__ == '__main__':
    unittest.main()
