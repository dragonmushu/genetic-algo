import unittest
from src.selection import RouletteWheel
from src.individual import  Individual


class TestRouletteWheel(unittest.TestCase):
    def test_probability_distribution_empty(self):
        values = []
        self.assertRaises(ValueError, RouletteWheel.create_probability_distribution, values)

    def test_probability_distribution_normal(self):
        values = [1, 2, 3, 4]
        expected_results = [0.1, 0.3, 0.6, 1.0]
        results = RouletteWheel.create_probability_distribution(values)
        self.assertEqual(len(expected_results), len(results))
        for i in range(0, len(results)):
            self.assertEqual(expected_results[i], results[i])

    def test_linear_search_normal(self):
        values = [0.1, 0.3, 0.6, 1.0]
        value = 0.5
        self.assertEqual(2, RouletteWheel.linear_search(values, value))

    def test_select_parents_empty(self):
        individuals = []
        self.assertRaises(ValueError, RouletteWheel.select_parents, individuals)

    def test_select_parents_two_elements(self):
        individual_1 = Individual(4, 1)
        individual_1.fitness = 1
        individual_2 = Individual(4, 1)
        individual_2.fitness = 2
        child_1, child_2 = RouletteWheel.select_parents([individual_1, individual_2])
        self.assertFalse(child_1 == child_2)


if __name__ == '__main__':
    unittest.main()
