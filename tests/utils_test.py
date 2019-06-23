import unittest
import src.utils as utils


class TestUtils(unittest.TestCase):

    def test_bit_set_all_zero(self):
        chromosome = 0
        position = 2
        self.assertFalse(utils.bit_set(chromosome, position))

    def test_bit_set(self):
        chromosome = 5
        position = 1
        self.assertTrue(utils.bit_set(chromosome, position))

    def test_bit_not_set(self):
        chromosome = 5
        position = 2
        self.assertFalse(utils.bit_set(chromosome, position))


if __name__ == '__main__':
    unittest.main()