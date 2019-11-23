import unittest

from vector import Vector
from particle import Particle


class TestCase(unittest.TestCase):

    def assertEqualVector(self, first: Vector, second: Vector, msg=None):
        self.assertEqual(first.x, second.x, msg)
        self.assertEqual(first.y, second.y, msg)

    def assertAlmostEqualVector(self, first: Vector, second: Vector, msg=None):
        self.assertAlmostEqual(first.x, second.x, msg)
        self.assertAlmostEqual(first.y, second.y, msg)

    def assertAlmostEqualParticle(self, first: Particle, second: Particle, msg=None):
        self.assertAlmostEqual(first.mass, second.mass, msg)
        self.assertAlmostEqualVector(first.position, second.position, msg)
        self.assertAlmostEqualVector(first.momentum, second.momentum, msg)


def main():
    unittest.main()
