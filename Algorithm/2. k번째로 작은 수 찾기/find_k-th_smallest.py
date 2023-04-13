import heapq

A = [int(x) for x in input().split()]
m = [0] * len(A)

for i in range(len(A)):
    if i == 0:
        m[i] = A[i]
    else:
        k = (i // 3) + 1
        heap = A[:i+1]  # 현재까지 입력된 수들 중에서
        heapq.heapify(heap)  # heap으로 만들어서
        for j in range(k-1):
            heapq.heappop(heap)  # k-1번 pop하고 
        m[i] = heap[0]  # 다음 수를 보면 k번째로 작은 수

print(sum(m))
