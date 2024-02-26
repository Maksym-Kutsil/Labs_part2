import unittest
from src.lab_1_2_3 import quick_sort

class TestQuickSort(unittest.TestCase):

    def test_empty_array(self):
        """Tests sorting an empty array."""
        self.assertEqual(quick_sort([]), [])

    def test_single_element_array(self):
        """Tests sorting an array with a single element."""
        self.assertEqual(quick_sort([5]), [5])

    def test_sorted_array(self):
        """Tests sorting an already sorted array."""
        self.assertEqual(quick_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_unsorted_array(self):
        """Tests sorting an unsorted array."""
        self.assertEqual(quick_sort([3, 1, 4, 2]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()



