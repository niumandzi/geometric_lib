import unittest
import math
from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):

    def test_area_positive_radius(self):
        # Arrange
        radius = 5
        expected_area = math.pi * radius * radius

        # Act
        result = area(radius)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_area_zero_radius(self):
        # Arrange
        radius = 0
        expected_area = 0

        # Act
        result = area(radius)

        # Assert
        self.assertEqual(result, expected_area)

    def test_perimeter_positive_radius(self):
        # Arrange
        radius = 5
        expected_perimeter = 2 * math.pi * radius

        # Act
        result = perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected_perimeter, places=5)

    def test_perimeter_zero_radius(self):
        # Arrange
        radius = 0
        expected_perimeter = 0

        # Act
        result = perimeter(radius)

        # Assert
        self.assertEqual(result, expected_perimeter)


if __name__ == "__main__":
    unittest.main()
