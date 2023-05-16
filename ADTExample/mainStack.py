from Stack import Stack

stack = Stack()
print(f"스택이 비었나요? {stack.isEmpty()}")
print("스택에 숫자 0~9를 추가합니다.")

for i in range(10):
    stack.push(i)

print(f"스택 크기: {stack.size()}")
print(f"peek: {stack.peek()}")
print(f"pop: {stack.pop()}")
print(f"peek: {stack.peek()}")
print(f"스택이 비었나요? {stack.isEmpty()}")
print(stack)