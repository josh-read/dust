import unittest

from vector import Vector


class TestCase(unittest.TestCase):

    def assertEqualVector(self, first: Vector, second: Vector, msg=None):
        self.assertEqual(first.x, second.x, msg)
        self.assertEqual(first.y, second.y, msg)

    def assertAlmostEqualVector(self, first: Vector, second: Vector, msg=None):
        self.assertAlmostEqual(first.x, second.x, msg)
        self.assertAlmostEqual(first.y, second.y, msg)


def main():
    unittest.main()
