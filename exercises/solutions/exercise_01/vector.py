"""Implementation of Vector class

Disclaimer
----------
The implementation is just enough for purpose of unit-testing and should not be seen
as a full implemenation of vector math. Many things are missing. 

"""

from __future__ import annotations

import math


class Vector:
    """Vector in 3D space. Supports vector math as addition, subtraction etc..."""

    def __init__(self, x: float, y: float, z: float):
        """Defines a point in 3D space or vector to be used for vector math.

        Parameters
        ----------
        x : float
            X coordinate
        y : float
            Y coordinate
        z : float
            Z coordinate
        """

        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x, y, z)

    def __mul__(self, other) -> Vector:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError(f"Type needs to be float or int, got {type(other)}")

    def __truediv__(self, other) -> Vector:
        if isinstance(other, (float, int)):
            return Vector(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError(f"Type needs to be float or int, got {type(other)}")

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    def unit_vector(self) -> Vector:
        """Returns unit vector of itself. """
        magnitude = abs(self)
        return Vector(self.x / magnitude, self.y / magnitude, self.z / magnitude)

