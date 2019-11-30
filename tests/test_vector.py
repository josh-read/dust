import pytest

from dust.vector import Vector


A = Vector(0, 0)
B = Vector(5, 0)
C = Vector(-3.14, 0)
D = Vector(3, 4)


class TestInit:

    def test_init_ints(self):
        Vector(-2, 4)

    def test_init_floats(self):
        Vector(2.245, -4.6345)

    def test_init_mixed(self):
        Vector(2, -4.6345)

    def test_init_complex(self):
        with pytest.raises(TypeError):
            Vector(2 + 1j, -4.6345 + 2.9521j)

    def test_init_string(self):
        with pytest.raises(TypeError):
            Vector('hello', 'world')


class TestAdd:

    def test_add_ints(self):
        assert Vector(-1, 4) + Vector(3, -6) == Vector(2, -2)

    def test_add_floats(self):
        assert Vector(2.245, -4.634) + Vector(23.420, -12.528) \
                                    == Vector(25.665, -17.162)

    def test_sum(self):
        assert sum([Vector(2.245, -4.634), Vector(23.420, -12.528)]) \
                                        == Vector(25.665, -17.162)


class TestMultiply:

    def test_multiply_scalar(self):
        assert 2 * Vector(-2, 4) == Vector(-4, 8)
        assert Vector(2, -4) * -2 == Vector(-4, 8)

    def test_multiply_float(self):
        assert 0.1 * Vector(-2.14, -8.23) == Vector(-0.214, -0.823)
        assert Vector(2.14, 8.23) * -0.1 == Vector(-0.214, -0.823)

    def test_multiply_by_zero(self):
        assert 0 * Vector(2, 4) == Vector(0, 0)
        assert Vector(2.14, -8.23) * 0 == Vector(0, 0)

    def test_multiply_bad_type(self):
        with pytest.raises(TypeError):
            (3 - 2j) * Vector(2, -3.1)
        with pytest.raises(TypeError):
            'test' * Vector(2, -3.1)


class TestDivide:

    def test_divide_int(self):
        assert Vector(2, -4) / -2 == Vector(-1, 2)

    def test_divide_float(self):
        assert Vector(2.14, 8.23) / -0.1 == Vector(-21.4, -82.3)

    def test_divide_by_zero(self):
        assert Vector(2.14, 8.23) / 0 == Vector(0, 0)

    def test_divide_wrong_order(self):
        with pytest.raises(TypeError):
            1.3 / Vector(2.21, 4.51)

    def test_multiply_bad_type(self):
        with pytest.raises(TypeError):
            Vector(2, -3.1) / (3 - 2j)
        with pytest.raises(TypeError):
            Vector(2, -3.1) / 'lel'


def test_scalar_dist():
    assert A.scalar_dist(B) == 5
    assert A.scalar_dist(C) == 3.14
    assert A.scalar_dist(D) == 5


def test_unit_vector():
    assert A.unit_vector() == Vector(0, 0)
    assert B.unit_vector() == Vector(1, 0)
    assert C.unit_vector() == Vector(-1, 0)
    assert D.unit_vector() == Vector(3/5, 4/5)
