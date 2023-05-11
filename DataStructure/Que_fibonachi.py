
from CircularQueue import *

q = CircularQueue()
q.enqueue(0)
q.enqueue(1)

print("피보나치 수열: ", 0, 1, end=' ')

for i in range(2,10):
    num1 = q.dequeue()
    num2 = q.peek()
    q.enqueue(num1 + num2)
    print(num1+num2, end=' ')
