import unittest

from src.genetic_algo import point_cross_over
from src.genetic_algo import center_cross_over
import src.utils as utils


class TestCrossOver(unittest.TestCase):

    def test_point_cross_over_zero(self):
        size = 4
        cross_point = 2
        chromosome_1 = int('0000', 2)
        chromosome_2 = int('0000', 2)
        expected = int('0000', 2)

        individual_1, individual_2 = point_cross_over(chromosome_1, chromosome_2, size, cross_point)
        self.assertEqual(individual_1, expected)
        self.assertEqual(individual_2, expected)

    def test_point_cross_over_max(self):
        size = 4
        cross_point = 2
        chromosome_1 = utils.max_binary_value(size)
        chromosome_2 = utils.max_binary_value(size)
        expected = utils.max_binary_value(size)

        individual_1, individual_2 = point_cross_over(chromosome_1, chromosome_2, size, cross_point)
        self.assertEqual(individual_1, expected)
        self.assertEqual(individual_2, expected)

    def test_point_cross_over_normal_even(self):
        size = 4
        chromosome_1 = int('1010', 2)
        chromosome_2 = int('1100', 2)
        expected_1 = int('1000', 2)
        expected_2 = int('1110', 2)

        individual_1, individual_2 = point_cross_over(chromosome_1, chromosome_2, size, 2)
        self.assertEqual(individual_2, expected_2)
        self.assertEqual(individual_1, expected_1)

    def test_point_cross_over_start(self):
        size = 4
        cross_point = 0
        chromosome_1 = int('1010', 2)
        chromosome_2 = int('1100', 2)
        expected_1 = int('1100', 2)
        expected_2 = int('1010', 2)

        individual_1, individual_2 = point_cross_over(chromosome_1, chromosome_2, size, cross_point)
        self.assertEqual(individual_1, expected_1)
        self.assertEqual(individual_2, expected_2)

    def test_point_cross_over_end(self):
        size = 4
        cross_point = 4
        chromosome_1 = int('1010', 2)
        chromosome_2 = int('1100', 2)
        expected_1 = int('1010', 2)
        expected_2 = int('1100', 2)

        individual_1, individual_2 = point_cross_over(chromosome_1, chromosome_2, size, cross_point)
        self.assertEqual(individual_1, expected_1)
        self.assertEqual(individual_2, expected_2)

    def test_point_cross_over_first_position(self):
        size = 4
        cross_point = 1
        chromosome_1 = int('0010', 2)
        chromosome_2 = int('1100', 2)
        expected_1 = int('0100', 2)
        expected_2 = int('1010', 2)

        individual_1, individual_2 = point_cross_over(chromosome_1, chromosome_2, size, cross_point)
        self.assertEqual(individual_1, expected_1)
        self.assertEqual(individual_2, expected_2)

    def test_point_cross_over_normal_uneven(self):
        size = 5
        cross_point = 3
        chromosome_1 = int('10101', 2)
        chromosome_2 = int('11100', 2)
        expected_1 = int('10100', 2)
        expected_2 = int('11101', 2)

        individual_1, individual_2 = point_cross_over(chromosome_1, chromosome_2, size, cross_point)
        self.assertEqual(individual_1, expected_1)
        self.assertEqual(individual_2, expected_2)

    def test_center_cross_over_even(self):
        size = 4
        chromosome_1 = int('1010', 2)
        chromosome_2 = int('1100', 2)
        expected_1 = int('1000', 2)
        expected_2 = int('1110', 2)

        individual_1, individual_2 = center_cross_over(chromosome_1, chromosome_2, size)
        self.assertEqual(individual_2, expected_2)
        self.assertEqual(individual_1, expected_1)

    def test_center_cross_over_uneven(self):
        size = 5
        chromosome_1 = int('10001', 2)
        chromosome_2 = int('11100', 2)
        expected_1 = int('10100', 2)
        expected_2 = int('11001', 2)

        individual_1, individual_2 = center_cross_over(chromosome_1, chromosome_2, size)
        self.assertEqual(individual_2, expected_2)
        self.assertEqual(individual_1, expected_1)


if __name__ == '__main__':
    unittest.main()
