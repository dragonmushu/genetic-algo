import unittest
import src.utils as utils


class TestUtils(unittest.TestCase):

    def test_max_binary_value_zero(self):
        size = 0
        self.assertEqual(0, utils.max_binary_value(size))

    def test_max_binary_value_one(self):
        size = 1
        self.assertEqual(1, utils.max_binary_value(size))

    def test_max_binary_value_normal(self):
        size = 4
        self.assertEqual(15, utils.max_binary_value(size))

    def test_random_two_elements_empty(self):
        elements = []
        self.assertRaises(Exception, utils.random_two_elements, elements)

    def test_random_two_elements_one(self):
        elements = [1]
        self.assertRaises(Exception, utils.random_two_elements, elements)

    def test_random_two_elements_two(self):
        elements = [1, 2]
        random_elements = utils.random_two_elements(elements)
        self.assertEqual(2, len(random_elements))
        self.assertNotEqual(random_elements[0], random_elements[1])
        self.assertTrue(random_elements[0] in elements)
        self.assertTrue(random_elements[1] in elements)

    def test_random_two_elements(self):
        elements = [1, 2, 3, 4, 5]
        random_elements = utils.random_two_elements(elements)
        self.assertEqual(2, len(random_elements))
        self.assertNotEqual(random_elements[0], random_elements[1])
        self.assertTrue(random_elements[0] in elements)
        self.assertTrue(random_elements[1] in elements)

    def test_bit_set_all_zero(self):
        chromosome = 0
        position = 2
        self.assertFalse(utils.bit_set(chromosome, position))

    def test_bit_set_final(self):
        chromosome = 10
        position = 4
        self.assertTrue(utils.bit_set(chromosome, position))

    def test_bit_set_initial(self):
        chromosome = 9
        position = 1
        self.assertTrue(utils.bit_set(chromosome, position))

    def test_bit_set_middle(self):
        chromosome = 18
        position = 2
        self.assertTrue(utils.bit_set(chromosome, position))

    def test_bit_not_set(self):
        chromosome = 5
        position = 2
        self.assertFalse(utils.bit_set(chromosome, position))


if __name__ == '__main__':
    unittest.main()