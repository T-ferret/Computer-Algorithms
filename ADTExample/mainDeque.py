import Deque 

deque = Deque.deque()

print(f"Deque is empty? {deque.isEmpty()}")
print(f"Deque에 숫자 0~9를 추가합니다.")

for i in range(10):
    deque.enqueue(i)

print(f"Deque 크기 : {deque.size()}")
print(f"peek : {deque.peek()}")
print(f"dequeue : {deque.dequeue()}")
print(f"peek : {deque.peek()}")
print(f"Deque is empty? {deque.isEmpty()}")
print()

print(f"Deque : {deque}")
print(f"dequeue_front :  {deque.dequeue_front()}")
print(f"peek : {deque.peek()}")
print(f"Deque : {deque}")
print()

print("enqueue_back(50) 수행")

deque.enqueue_back(50)

print(f"peek {deque.peek()}")
print(f"Deque : {deque}")