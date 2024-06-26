import unittest
from src.max_flow import max_flow


class TestFlowersMaxFlow(unittest.TestCase):
    def test_farms_stores_graph(self):
        result = max_flow("../resourses/roads.csv")
        self.assertEqual(result, 15)

    def test_empty_input(self):
        result = max_flow("../resourses/empty_roads.csv")
        self.assertEqual(result, None)