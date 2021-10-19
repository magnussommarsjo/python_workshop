"""Solution example of exercise_01

This test_suite uses simple syntax and functionality to test the funtionality of Vector
class

Here we use 'pytest.raises(...)' context manager to test that functions properly raises 
certain types of exeptions 
"""

import math
import pytest

from solutions.exercise_01.vector import Vector


def test_init():
    """Checks that initialization of arguments are in correct order"""
    vector = Vector(1, 2, 3)
    assert vector.x == 1
    assert vector.y == 2
    assert vector.z == 3


def test_add():
    """Addition should be correct both for negative and positive values"""
    vector_1 = Vector(1, 2, 3)
    vector_2 = Vector(-1, -2, -3)

    should_be_zero = vector_1 + vector_2
    assert should_be_zero.x == 0
    assert should_be_zero.y == 0
    assert should_be_zero.z == 0

    double = vector_1 + vector_1
    assert double.x == 2
    assert double.y == 4
    assert double.z == 6


def test_subtract():
    """Subtraction should be correct both for negative and positive values"""
    vector_1 = Vector(1, 2, 3)
    vector_2 = Vector(-1, -2, -3)

    should_be_zero = vector_1 - vector_1
    assert should_be_zero.x == 0
    assert should_be_zero.y == 0
    assert should_be_zero.z == 0

    double = vector_1 - vector_2
    assert double.x == 2
    assert double.y == 4
    assert double.z == 6


def test_multiplication():
    vector_1 = Vector(1, 2, 3)
    double = vector_1 * 2.0
    assert double.x == 2
    assert double.y == 4
    assert double.z == 6


def test_multiplication_raises_error():
    vector_1 = Vector(1, 2, 3)

    with pytest.raises(TypeError):
        _ = vector_1 * vector_1

    with pytest.raises(TypeError):
        _ = vector_1 * "2"


def test_division():
    vector_1 = Vector(1, 2, 3)
    double = vector_1 / 2.0
    assert double.x == 0.5
    assert double.y == 1
    assert double.z == 1.5


def test_division_raises_error():
    vector_1 = Vector(1, 2, 3)

    with pytest.raises(TypeError):
        _ = vector_1 / vector_1

    with pytest.raises(TypeError):
        _ = vector_1 / "2"


def test_abs():
    """Test abs/length of vector"""

    assert abs(Vector(1, 0, 0)) == 1
    assert abs(Vector(-1, 0, 0)) == 1
    assert abs(Vector(1, 1, 1)) == math.sqrt(3)


def test_equality():
    assert Vector(1, 1, 1) == Vector(1, 1, 1)


def test_inequality():
    assert Vector(1, 1, 1) != Vector(0, 0, 0)


def test_unit_vector():
    vector = Vector(10, 0, 0)
    u_vector = vector.unit_vector()
    assert u_vector.x == 1
    assert u_vector.y == 0
    assert u_vector.z == 0

