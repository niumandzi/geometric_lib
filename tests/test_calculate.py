import unittest
import math
from calculate import calc


class TestCalcFunctionality(unittest.TestCase):

    def test_circle_area_via_calc(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [5]
        expected_result = math.pi * size[0] ** 2

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_circle_perimeter_via_calc(self):
        # Arrange
        fig = 'circle'
        func = 'perimeter'
        size = [5]
        expected_result = 2 * math.pi * size[0]

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_square_area_via_calc(self):
        # Arrange
        fig = 'square'
        func = 'area'
        size = [4]
        expected_result = size[0] ** 2

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_square_perimeter_via_calc(self):
        # Arrange
        fig = 'square'
        func = 'perimeter'
        size = [4]
        expected_result = 4 * size[0]

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_negative_size_via_calc(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [-5]

        # Act & Assert
        with self.assertRaises(AssertionError) as cm:
            calc(fig, func, size)
        self.assertEqual(str(cm.exception), "Size parameters must be positive")

    def test_size_mismatch_via_calc(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [5, 10]

        # Act & Assert
        with self.assertRaises(TypeError):
            calc(fig, func, size)

    def test_unsupported_figure_via_calc(self):
        # Arrange
        fig = 'triangle'
        func = 'area'
        size = [3, 4, 5]

        # Act & Assert
        with self.assertRaises(AssertionError) as cm:
            calc(fig, func, size)
        self.assertEqual(str(cm.exception), "Unknown figure: triangle")


if __name__ == "__main__":
    unittest.main()
