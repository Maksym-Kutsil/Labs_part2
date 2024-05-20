class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapyfy_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent].priority > self.heap[i].priority:
                self.swap(i, parent)
            i = parent

    def heapyfy_down(self, i):
        while 2 * i + 1 < len(self.heap):
            left = 2 * i + 1
            right = 2 * i + 2
            less_priority = i
            if left < len(self.heap) and self.heap[left].priority < self.heap[less_priority].priority:
                less_priority = left
            if right < len(self.heap) and self.heap[right].priority < self.heap[less_priority].priority:
                less_priority = right
            if i != less_priority:
                self.swap(i, less_priority)
                i = less_priority

            else:
                break

    def add(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self.heapyfy_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapyfy_down(0)
        return root

    def display(self):
        for node in self.heap:
            print(f"Value: {node.value}, Priority: {node.priority}")

