class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Queue:", self.items)

# Example usage
q = Queue()
q.enqueue("Apple")
q.enqueue("Banana")
q.enqueue("Cherry")
q.display()
print("Front item:", q.peek())
print("Dequeued item:", q.dequeue())
q.display()
