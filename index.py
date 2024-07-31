#Class name is Heap
class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):

        # Adding a new value to the end of the heap using append in Python lists
        self.heap.append(value)

        #maintaining the heap property
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        parent_index = (index - 1) // 2

        # Check if the current node is greater than its parent
        while index > 0 and self.heap[index] > self.heap[parent_index]:

            # Swap the current node with its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def get_heap(self):
        return self.heap

max_heap = Heap()
max_heap.insert(77)
max_heap.insert(50)
max_heap.insert(60)
max_heap.insert(30)
max_heap.insert(22)
max_heap.insert(44)
max_heap.insert(55)
max_heap.insert(55)

print(max_heap.get_heap())
