import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):

    def test_area_positive_side(self):
        # Arrange
        side_length = 5
        expected_area = 25

        # Act
        result = area(side_length)

        # Assert
        self.assertEqual(result, expected_area)

    def test_area_zero_side(self):
        # Arrange
        side_length = 0
        expected_area = 0

        # Act
        result = area(side_length)

        # Assert
        self.assertEqual(result, expected_area)

    def test_perimeter_positive_side(self):
        # Arrange
        side_length = 5
        expected_perimeter = 20

        # Act
        result = perimeter(side_length)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_zero_side(self):
        # Arrange
        side_length = 0
        expected_perimeter = 0

        # Act
        result = perimeter(side_length)

        # Assert
        self.assertEqual(result, expected_perimeter)


if __name__ == "__main__":
    unittest.main()
