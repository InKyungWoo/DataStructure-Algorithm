
from LinkedQueue import *

q = LinkedQueue()

print("0~7 정수 큐에 삽입")
for i in range(8):
    q.enqueue(i)
print("size: ", q.size())
q.display(); print()

print("큐에서 4개 삭제")
for i in range(4):
    q.dequeue()
print("size: ", q.size())
q.display(); print()

print("8~13 정수 큐에 삽입")
for i in range(8,14):
    q.enqueue(i)
print("size: ", q.size())
q.display(); print()

