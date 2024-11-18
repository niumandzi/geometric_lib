import unittest
from triangle import area, perimeter
import math


class TestTriangleFunctions(unittest.TestCase):

    def test_area_valid_triangle(self):
        # Arrange
        a, b, c = 3, 4, 5
        s = (a + b + c) / 2
        expected_area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Act
        result = area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_perimeter_valid_triangle(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected_perimeter = a + b + c

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_perimeter)


if __name__ == "__main__":
    unittest.main()
