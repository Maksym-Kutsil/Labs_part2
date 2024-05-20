import unittest
from src.w_chain import *


class TestWchain(unittest.TestCase):
    def test_default_condition(self):
        write_output_file("../resourses/w_chain_input.txt", "../resourses/w_chain_out.txt")
        with open("../resourses/w_chain_out.txt", "r", encoding="utf-8") as w_chain_out:
            result = int(w_chain_out.readline())
        self.assertEqual(result, 6)

    def test_empty_wchain(self):
        write_output_file("../resourses/w_chain_empty_input.txt", "../resourses/w_chain_empty_output.txt")
        with open("../resourses/w_chain_empty_output.txt", "r", encoding="utf-8") as w_chain_out:
            result = int(w_chain_out.readline())
        self.assertEqual(result, 0)