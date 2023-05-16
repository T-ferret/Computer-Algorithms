from node import Node

class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)
    
    def push(self, item):
        self.head = Node(item, self.head) # Node함수 안에서 self.head는 이전 노드의 주소(참조값)를 가리키고, left 변수 self.head는 item의 주소(참조값)를 가리킴
        self.count += 1

    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print("Stack is empty.")

    def size(self):
        return self.count
    
    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print("Stack is empty.")

    def _printlist(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()