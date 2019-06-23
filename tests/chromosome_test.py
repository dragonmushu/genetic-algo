import unittest
from src.chromosome import generate_random_chromosome
from src.chromosome import generate_chromosome_from_bits


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


if __name__ == '__main__':
    unittest.main()