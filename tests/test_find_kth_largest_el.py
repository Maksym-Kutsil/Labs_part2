import unittest
from src.find_kth_largest_el import *


class TestQuickSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        self.assertEqual(quick_sort(arr), [])

    def test_single_element_array(self):
        arr = [3]
        self.assertEqual(quick_sort(arr), [3])

    def test_sorted_array(self):
        arr = [2, 3, 5, 10, 14]
        self.assertEqual(quick_sort(arr), [14, 10, 5, 3, 2])

    def test_unsorted_array(self):
        arr = [5, 3, 10, 2, 14]
        self.assertEqual(quick_sort(arr), [14, 10, 5, 3, 2])

    def test_find_largest_el(self):
        array = [5, 3, 10, 2, 14]
        self.assertEqual(find_kth_largest_el(array, 1), "1 найбільший елемент : 14, індекс елементу в масиві : 4")
        self.assertEqual(find_kth_largest_el(array, 2), "2 найбільший елемент : 10, індекс елементу в масиві : 2")
        self.assertEqual(find_kth_largest_el(array, 3), "3 найбільший елемент : 5, індекс елементу в масиві : 0")
        self.assertEqual(find_kth_largest_el(array, 4), "4 найбільший елемент : 3, індекс елементу в масиві : 1")
        self.assertEqual(find_kth_largest_el(array, 5), "5 найбільший елемент : 2, індекс елементу в масиві : 3")

    def test_index(self):
        array = [7, 9, 12, 3, 6, 5, 15, 18, 10]
        self.assertEqual(find_kth_largest_el(array, 1), "1 найбільший елемент : 18, індекс елементу в масиві : 7")

if __name__ == '__main__':
    unittest.main()
