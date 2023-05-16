from node import Node

class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)
    
    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print("Queue is empty.")

    def size(self):
        return self.count
    
    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("Queue is empty.")

    def _print(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()