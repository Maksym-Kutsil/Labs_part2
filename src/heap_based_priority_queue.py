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
            smallest = i
            if left < len(self.heap) and self.heap[left].priority < self.heap[smallest].priority:
                smallest = left
            if right < len(self.heap) and self.heap[right].priority < self.heap[smallest].priority:
                smallest = right
            if i != smallest:
                self.swap(i, smallest)
                i = smallest
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
        if len(self.heap) > 0:
            self.heapyfy_down(0)
        return root

    def display(self):
        for node in self.heap:
            print(f"Значення: {node.value}, Пріоритет: {node.priority}")


if __name__ == "__main__":
    pq = PriorityQueue()

    pq.add("Завдання 1", 4)
    pq.add("Завдання 2", 3)
    pq.add("Завдання 3", 1)
    pq.add("Завдання 15", 8)
    pq.add("Завдання 5", 2)
    pq.add("Завдання 10", 11)

    pq.display()

    deleted_item = pq.delete()
    print(f"Видалений елемент: {deleted_item.value} (Пріоритет: {deleted_item.priority})")
    pq.display()
