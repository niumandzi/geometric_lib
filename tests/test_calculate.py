import math
import unittest
from calculate import calc


class TestCalculateFunction(unittest.TestCase):

    def test_valid_circle_area(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [5]
        expected_result = math.pi * size[0] ** 2

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_valid_square_perimeter(self):
        # Arrange
        fig = 'square'
        func = 'perimeter'
        size = [4]
        expected_result = 4 * size[0]

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_invalid_figure(self):
        # Arrange
        fig = 'triangle'
        func = 'area'
        size = [5]

        # Act & Assert
        with self.assertRaises(AssertionError) as cm:
            calc(fig, func, size)
        self.assertEqual(str(cm.exception), "Unknown figure: triangle")

    def test_invalid_function(self):
        # Arrange
        fig = 'circle'
        func = 'volume'
        size = [5]

        # Act & Assert
        with self.assertRaises(AssertionError) as cm:
            calc(fig, func, size)
        self.assertEqual(str(cm.exception), "Unknown function: volume")

    def test_negative_size(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [-5]

        # Act & Assert
        with self.assertRaises(AssertionError) as cm:
            calc(fig, func, size)
        self.assertEqual(str(cm.exception), "Size parameters must be positive")

    def test_size_mismatch(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [5, 10]

        # Act & Assert
        with self.assertRaises(TypeError):
            calc(fig, func, size)


if __name__ == "__main__":
    unittest.main()
