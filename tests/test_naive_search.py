import unittest
from src.naive_search import naive_search


class TestNaiveSearch(unittest.TestCase):
    def test_empty_needle(self):
        haystack = "hello"
        needle = ""
        result_index, result_comparisons = naive_search(haystack, needle)
        self.assertEqual(result_index, None)
        self.assertEqual(result_comparisons, 0)

    def test_needle_not_found(self):
        haystack = "hello world"
        needle = "python"
        result_index, result_comparisons = naive_search(haystack, needle)
        self.assertEqual(result_index, None)
        self.assertEqual(result_comparisons, 11)

    def test_needle_found(self):
        haystack = "test1 test2"
        needle = "test2"
        result_index, result_comparisons = naive_search(haystack, needle)
        self.assertEqual(result_index, 6)
        self.assertEqual(result_comparisons, 11)


if __name__ == "__main__":
    unittest.main()
