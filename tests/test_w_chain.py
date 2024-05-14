import unittest
from src.w_chain import *


class TestWordChain(unittest.TestCase):
    def test_word_chain(self):
        result = word_chain("../resourses/w_chain_input.txt")
        self.assertEqual(result, 6)

    def test_empty_input(self):
        result = word_chain("../resourses/w_chain_empty_input.txt")
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()

