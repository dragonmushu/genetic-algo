import unittest
from src.chromosome import *


class TestChromosome(unittest.TestCase):

    def test_generate_empty_chromosome(self):
        chromosome = generate_random_chromosome(0)
        print(chromosome)
        self.assertEqual(chromosome, 0)

    def test_generate_random_chromosome(self):
        max_val = 7
        for i in range(0, 10):
            chromosome = generate_random_chromosome(3)
            self.assertTrue(0 <= chromosome <= max_val)

    def test_generate_chromosome_from_bits_zero(self):
        chromosome = generate_chromosome_from_bits('000')
        self.assertEqual(chromosome, 0)

    def test_generate_chromosome_from_bits_max(self):
        chromosome = generate_chromosome_from_bits('111')
        self.assertEqual(chromosome, 7)

    def test_generate_chromosome_from_bits_normal(self):
        chromosome = generate_chromosome_from_bits('101')
        self.assertEqual(chromosome, 5)

    def test_chromosome_subset_value_zero(self):
        chromosome = 0
        start = 2
        length = 1
        self.assertEqual(0, chromosome_subset_value(chromosome, start, length))

    def test_chromosome_subset_value_normal(self):
        chromosome = 77  # 1001101
        start = 2
        length = 3
        subset = 6  # 110
        self.assertEqual(subset, chromosome_subset_value(chromosome, start, length))

    def test_chromosome_subset_value_ones(self):
        chromosome = 15  # 1111
        start = 2
        length = 2
        subset = 3  # 11
        self.assertEqual(subset, chromosome_subset_value(chromosome, start, length))

    def test_chromosome_subset_value_zero_start(self):
        chromosome = 15  # 1111
        start = 0
        length = 2
        self.assertRaises(ValueError, chromosome_subset_value, chromosome, start, length)

    def test_chromosome_subset_value_past_length(self):
        chromosome = 15  # 1111
        start = 3
        length = 4
        subset = 3  # 0011
        self.assertEqual(subset, chromosome_subset_value(chromosome, start, length))


if __name__ == '__main__':
    unittest.main()