import unittest

from src.genetic_algo import GenGo


class TestCrossOver(unittest.TestCase):

    def setUp(self):
        self.gengo = GenGo();

    def test_default_select_generation_empty(self):
        individuals = []
        next_generations = self.gengo.__default_select_generation__(individuals)
        self.assertIsNone(next_generations)


if __name__ == '__main__':
    unittest.main()
