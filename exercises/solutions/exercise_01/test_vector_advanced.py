"""Solution example of exercise_01

This test_suite uses more advanced syntax and functinality to test the Vector class.

Exactly the same test is performed as last time but some more functinality to avoid 
repeating ourself is implemented.

Here we use some techniques:
-   Helper functions
    If you assert certain things in multiple test_functions, it can be helpful to cretae
    a specific method for it.

-   @pytest.mark.parameterize decorator
    This lets you run same test multiple times with varying arguments. A whole new test 
    will occur and previous arguments will not break test for the following arguments. 

"""

import pytest
import math

from solutions.exercise_01.vector import Vector


def assert_vector_has_values(vector: Vector, x: float, y: float, z: float):
    """Helper function to check values in Vector"""
    assert vector.x == x
    assert vector.y == y
    assert vector.z == z


@pytest.fixture
def vector_1():
    return Vector(1, 2, 3)


@pytest.fixture
def vector_2():
    return Vector(-1, -2, -3)


def test_init():
    """Checks that initialization of arguments are in correct order"""
    vector = Vector(1, 2, 3)
    assert_vector_has_values(vector, 1, 2, 3)


def test_add(vector_1: Vector, vector_2: Vector):
    """Addition should be correct both for negative and positive values"""

    should_be_zero = vector_1 + vector_2
    assert_vector_has_values(should_be_zero, 0, 0, 0)

    double = vector_1 + vector_1
    assert_vector_has_values(double, 2, 4, 6)


def test_subtract(vector_1: Vector, vector_2: Vector):
    """Subtraction should be correct both for negative and positive values"""

    should_be_zero = vector_1 - vector_1
    assert_vector_has_values(should_be_zero, 0, 0, 0)

    double = vector_1 - vector_2
    assert_vector_has_values(double, 2, 4, 6)


def test_multiplication(vector_1: Vector):
    double = vector_1 * 2.0
    assert_vector_has_values(double, 2, 4, 6)


@pytest.mark.parametrize("other", [Vector(1, 2, 3), "2"])
def test_multiplication_raises_error(other, vector_1: Vector):
    with pytest.raises(TypeError):
        _ = vector_1 * other


def test_division(vector_1: Vector):
    double = vector_1 / 2.0
    assert_vector_has_values(double, 0.5, 1, 1.5)


@pytest.mark.parametrize("other", [Vector(1, 2, 3), "2"])
def test_division_raises_error(other, vector_1: Vector):
    with pytest.raises(TypeError):
        _ = vector_1 / other


@pytest.mark.parametrize(
    ["input_vector", "expected_result"],
    [(Vector(1, 0, 0), 1), (Vector(-1, 0, 0), 1), (Vector(1, 1, 1), math.sqrt(3))],
)
def test_abs(input_vector: Vector, expected_result: float):
    """Test abs/length of vector"""
    assert abs(input_vector) == expected_result


def test_equality():
    assert Vector(1, 1, 1) == Vector(1, 1, 1)


def test_inequality():
    assert Vector(1, 1, 1) != Vector(0, 0, 0)


def test_unit_vector():
    vector = Vector(10, 0, 0).unit_vector()
    assert_vector_has_values(vector, 1, 0, 0)
