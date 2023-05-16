from Stack import Stack

class Queue(object):
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def _transfer(self):
        while not self.in_stack.isEmpty():
            self.out_stack.push(self.in_stack.pop())
            # print(self.out_stack)
    
    def enqueue(self, item):
        self.in_stack.push(item)
        # print(self.in_stack)

    def dequeue(self):
        if self.out_stack.isEmpty():
            self._transfer()
        if not self.out_stack.isEmpty():
            return self.out_stack.pop()
        else:
            print("Queue is empty.")

    def size(self):
        return self.in_stack.size() + self.out_stack.size()
    
    def peek(self):
        if self.out_stack.isEmpty():
            self._transfer()
        if not self.out_stack.isEmpty():
            return self.out_stack.peek()
        else:
            print("Queue is empty.")

    def __repr__(self):
        if self.out_stack.isEmpty():
            self._transfer()
        if not self.out_stack.isEmpty():
            return repr(self.out_stack)
        else:
            print("Queue is empty.")

    def isEmpty(self):
        return self.in_stack.isEmpty() and self.out_stack.isEmpty()