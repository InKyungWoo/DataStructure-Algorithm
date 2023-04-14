import heapq

def find_kth_smallest(heap, k):
    # heap에서 k번째로 작은 수를 찾음
    for _ in range(k-1):
        heapq.heappop(heap)
    
    return heapq.heappop(heap)

def find_m_sum():
    A = [int(x) for x in input().split()]   # 입력받은 숫자들을 리스트 A에 저장
    n = len(A)
    m = [0] * n
    
    heapq.heapify(A)   # 리스트 A를 힙으로 만듦
    
    heap = []   # A[0]부터 A[i]까지의 부분리스트를 저장하기 위한 heap
    for i in range(n):
        heapq.heappush(heap, A[i])
        k = i // 3 + 1
        m[i] = find_kth_smallest(heap[:i+1], k)
    
    return sum(m)

print(find_m_sum())
