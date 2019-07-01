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

    def test_gene_value_first_bits(self):
        chromosome = 67  # 1000011
        chromosome_size = 7
        start_pos = 1
        end_pos = 3
        individual = Individual(chromosome_size=chromosome_size, chromosome=chromosome)
        self.assertEqual(3, individual.gene_value(start_pos, end_pos))

    def test_gene_value_end_bits(self):
        chromosome = 67  # 1000011
        chromosome_size = 7
        start_pos = 6
        end_pos = 7
        individual = Individual(chromosome_size=chromosome_size, chromosome=chromosome)
        self.assertEqual(2, individual.gene_value(start_pos, end_pos))

    def test_gene_value_past_limit(self):
        chromosome = 67  # 1000011
        chromosome_size = 7
        start_pos = 6
        end_pos = 8
        individual = Individual(chromosome_size=chromosome_size, chromosome=chromosome)
        self.assertRaises(ValueError, individual.gene_value, start_pos, end_pos)

    def test_gene_value_at_zero(self):
        chromosome = 67  # 1000011
        chromosome_size = 7
        start_pos = 0
        end_pos = 4
        individual = Individual(chromosome_size=chromosome_size, chromosome=chromosome)
        self.assertRaises(ValueError, individual.gene_value, start_pos, end_pos)

    def test_gene_value_all(self):
        chromosome = 67  # 1000011
        chromosome_size = 7
        start_pos = 1
        end_pos = 7
        individual = Individual(chromosome_size=chromosome_size, chromosome=chromosome)
        self.assertEqual(67, individual.gene_value(start_pos, end_pos))

    def tearDown(self):
        self.individual.clear_metrics()


if __name__ == '__main__':
    unittest.main()