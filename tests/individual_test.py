import unittest
from src.individual import generate_random_chromosome


class TestIndividual(unittest.TestCase):

    def test_individual_generate_empty_chromosome(self):
        chromosome = generate_random_chromosome(0)
        print(chromosome)
        self.assertEqual(chromosome, 0)

    def test_individual_generate_random_chromosome(self):
        max_val = 7
        for i in range(0, 10):
            chromosome = generate_random_chromosome(3)
            self.assertTrue(0 < chromosome < max_val)


if __name__ == '__main__':
    unittest.main()