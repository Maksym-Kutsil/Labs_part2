from src.heap_based_priority_queue import *
import unittest

class PriorityQueueTest(unittest.TestCase):
   def test_add(self):
       pq = PriorityQueue()
       pq.add("Завдання 1", 4)
       pq.add("Завдання 2", 3)
       pq.add("Завдання 3", 1)
       pq.add("Завдання 15", 8)
       pq.add("Завдання 5", 2)
       pq.add("Завдання 10", 11)

       self.assertEqual(len(pq.heap), 6)
       self.assertEqual(pq.heap[0].priority, 1)
       self.assertEqual(pq.heap[1].priority, 2)
       self.assertEqual(pq.heap[-1].priority, 11)

   def test_delete(self):
       pq = PriorityQueue()
       pq.add("Завдання 1", 4)
       pq.add("Завдання 2", 3)
       pq.add("Завдання 3", 1)
       pq.add("Завдання 15", 8)
       pq.add("Завдання 5", 2)
       pq.add("Завдання 10", 11)

       pq.delete()
       self.assertEqual(len(pq.heap), 5)
       self.assertEqual(pq.heap[0].priority, 2)


   def test_empty_queue(self):
       pq = PriorityQueue()
       self.assertEqual(pq.delete(), None)
       self.assertEqual(len(pq.heap), 0)

if __name__ == "__main__":
   unittest.main()
