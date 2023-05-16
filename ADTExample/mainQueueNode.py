from QueueNode import LinkedQueue as LQueue

queue = LQueue()

print(f"큐가 비었나요? {queue.isEmpty()}")
print("큐에 숫자 0~9를 추가합니다.")

for i in range(10):
    queue.enqueue(i)

print(f"큐가 비었나요? {queue.isEmpty()}")
queue._print()

print(f"큐 크기: {queue.size()}")
print(f"peek: {queue.peek()}")
print(f"dequeue: {queue.dequeue()}")
print(f"peek: {queue.peek()}")
print(f"큐가 비었나요? {queue.isEmpty()}")
queue._print()