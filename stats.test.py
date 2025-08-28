import unittest
import math
import stats as statistics

class TestStats(unittest.TestCase):
    def test_min_max_avg(self):
        result = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
        eps = 0.001
        self.assertAlmostEqual(result["avg"], 4.525, delta=eps)
        self.assertAlmostEqual(result["max"], 8.9, delta=eps)
        self.assertAlmostEqual(result["min"], 1.5, delta=eps)

    def test_empty_input(self):
        result = statistics.calculateStats([])
        self.assertTrue(math.isnan(result["avg"]))
        self.assertTrue(math.isnan(result["max"]))
        self.assertTrue(math.isnan(result["min"]))

    def test_input_with_nan(self):
        result = statistics.calculateStats([1.0, float("nan"), 3.0])
        eps = 0.001
        self.assertAlmostEqual(result["avg"], 2.0, delta=eps)
        self.assertAlmostEqual(result["max"], 3.0, delta=eps)
        self.assertAlmostEqual(result["min"], 1.0, delta=eps)

    def test_invalid_values(self):
        result = statistics.calculateStats([1.0, 2.0, 1e100])
        self.assertTrue(math.isnan(result["avg"]))
        self.assertTrue(math.isnan(result["max"]))
        self.assertTrue(math.isnan(result["min"]))


if __name__ == "__main__":
    unittest.main()
