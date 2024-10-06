class Queue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.front = 0
        self.rear = -1
        self.capacity = capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full (Overflow condition).")
            return
        self.rear += 1
        self.arr[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty (Underflow condition).")
            return
        removed_item = self.arr[self.front]
        # Shift elements to the left
        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.rear -= 1
        self.size -= 1
        print(f"Dequeued item: {removed_item}")

    def front_element(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        return self.arr[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()


queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  # Output: Queue elements: 10 20 30
print("Front element:", queue.front_element())  # Output: Front element: 10
queue.dequeue()  # Output: Dequeued item: 10
queue.display()  # Output: Queue elements: 20 30
