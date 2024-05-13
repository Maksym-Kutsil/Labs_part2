from ..src.heap_based_priority_queue import *
import unittest

class PriorityQueueTest(unittest.TestCase):
    def test_add(self):
        pq = PriorityQueue()
        pq.add(1, 4)
        pq.add(2, 3)
        pq.add(3, 1)
        pq.add(25, 8)
        pq.add(5, 2)
        pq.add(10, 11)

        self.assertEqual(len(pq.heap), 6)
        self.assertEqual(pq.heap[0].priority, 1)
        self.assertEqual(pq.heap[1].priority, 2)
        self.assertEqual(pq.heap[-1].priority, 11)

    def test_delete(self):
        pq = PriorityQueue()

        pq.add(1, 4)
        pq.add(2, 3)
        pq.add(3, 1)
        pq.add(15, 8)
        pq.add(5, 2)
        pq.add(10, 11)

        pq.delete()
        self.assertEqual(len(pq.heap), 5)
        self.assertEqual(pq.heap[0].priority, 2)

    def test_empty_queue(self):
        pq = PriorityQueue()
        pq.add(1, 10)
        pq.delete()
        self.assertEqual(len(pq.heap), 0)
        self.assertEqual(pq.delete(), None)

if __name__ == "__main__":
    unittest.main()

