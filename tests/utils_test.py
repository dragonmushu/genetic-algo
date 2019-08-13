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

    def test_set_bit_all_zero(self):
        chromosome = 0
        position = 1
        self.assertEqual(1, utils.set_bit(chromosome, position))

    def test_set_bit_final(self):
        chromosome = 7  # 0111
        position = 4
        expected = 15  # 1111
        self.assertEqual(expected, utils.set_bit(chromosome, position))

    def test_set_bit_already_set(self):
        chromosome = 7
        position = 3
        expected = 7
        self.assertEqual(expected, utils.set_bit(chromosome, position))

    def test_unset_bit_initial(self):
        chromosome = 1
        position = 1
        expected = 0
        self.assertEqual(expected, utils.unset_bit(chromosome, position))

    def test_unset_bit_final(self):
        chromosome = 7
        position = 3
        expected = 3
        self.assertEqual(expected, utils.unset_bit(chromosome, position))

    def test_unset_bit_already_unset(self):
        chromosome = 5  # 101
        position = 2
        expected = 5
        self.assertEqual(expected, utils.unset_bit(chromosome, position))

    def test_flip_bit_initial_val(self):
        chromosome = 6  # 110
        position = 1
        expected = 7  # 111
        self.assertEqual(expected, utils.flip_bit(chromosome, position))

    def test_flip_bit_final_val(self):
        chromosome = 7
        position = 3
        expected = 3
        self.assertEqual(expected, utils.flip_bit(chromosome, position))


if __name__ == '__main__':
    unittest.main()