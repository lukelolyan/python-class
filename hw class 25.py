class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full (Overflow condition).")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty (Underflow condition).")
            return

        removed_item = self.queue[self.front]
        if self.front == self.rear:
          
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Dequeued: {removed_item}")

    def front_element(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()

circular_queue = CircularQueue(5)
circular_queue.enqueue(10)
circular_queue.enqueue(20)
circular_queue.enqueue(30)
circular_queue.enqueue(40)
circular_queue.enqueue(50)
circular_queue.display()  # Output: Queue elements: 10 20 30 40 50
circular_queue.dequeue()  # Output: Dequeued: 10
circular_queue.display()  # Output: Queue elements: 20 30 40 50
circular_queue.enqueue(60)
circular_queue.display()  # Output: Queue elements: 20 30 40 50 60
