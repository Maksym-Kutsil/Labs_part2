from src.tribes import *
import unittest

class TestCountPossiblePairs(unittest.TestCase):
    def test_1(self):
        case_1 = [
            [1, 2],
            [2, 4],
            [3, 5]
        ]
        self.assertEqual(count_possible_pairs(3, case_1), 4)

    def test_2(self):
        case_2 = [
            [1, 2],
            [1, 2],
            [1, 2]
        ]
        self.assertEqual(count_possible_pairs(3, case_2), 0)

    def test_3(self):
        case_3 = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10]
        ]
        self.assertEqual(count_possible_pairs(5, case_3), 20)

if __name__ == '__main__':
    unittest.main()
