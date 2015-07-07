__author__ = 'd.tabakerov'


from unittest import TestCase

from aggregator.aggregator import calculate


class AggregatorTest(TestCase):

    def test_arithmetic_mean(self):
        self.assertAlmostEqual(calculate({1: 10, 2: 20, 3: 30}), (10.0+20.0+30.0)/3, delta=0.001)