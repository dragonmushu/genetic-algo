import unittest
from src.individual import Individual


class TestIndividual(unittest.TestCase):

    def setUp(self):
        self.individual = Individual(chromosome_size=10, chromosome=0)

    def test_add_metric_value(self):
        key = 'metric'
        val = 5
        self.individual.add_metric(key, val)
        self.assertEqual(1, len(self.individual.metrics))
        self.assertEqual(5, self.individual.get_metric(key))

    def test_add_metric_overrides(self):
        key = 'metric'
        val_1 = 5
        val_2 = 3
        self.individual.add_metric(key, val_1)
        self.individual.add_metric(key, val_2)
        self.assertEqual(1, len(self.individual.metrics))
        self.assertEqual(3, self.individual.get_metric(key))

    def test_add_metric_averaging(self):
        key = 'metric'
        val_1 = 5
        val_2 = 3
        self.individual.add_metric(key, val_1, average=True)
        self.individual.add_metric(key, val_2, average=True)
        self.assertEqual(1, len(self.individual.metrics))
        self.assertEqual(4, self.individual.get_metric(key))

    def tearDown(self):
        self.individual.clear_metrics()


if __name__ == '__main__':
    unittest.main()