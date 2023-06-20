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
import heapq

# 입력받은 수를 리스트 A에 저장
A = [int(x) for x in input().split()]

# m[i]를 저장할 빈 리스트 생성
m = [0] * len(A)

for i in range(len(A)):
    if i == 0:
        m[i] = A[i]
    else:
        k = (i // 3) + 1
        heap = A[:i+1]  # 지금까지 입력된 수
        heapq.heapify(heap)  # heap으로 만들기 -> O(n*logn)
				
				# k-1 번 반복하여 pop 하면 그 다음수인 heap[0]이 k번째로 작은 수
        for j in range(k-1):  			# (k-1)번 반복
            heapq.heappop(heap)  		# O(k * logn)
        m[i] = heap[0]							# O(1)

print(sum(m))


'''
이 코드는 입력된 수를 리스트 A에 저장하고, 각 i에 대해 m[i] 값을 구한다. 이 떄, m[i]는 A[i]까지의 수 중에서 (i//3 + 1)번째로 작은 값이다.
이를 구현하기 위해 heap 자료구조를 이용하였다. 현재까지 입력된 수들 중에서 i번째 수까지 heapq.heapify 함수를 이용해 heap을 만들고, for문을 반복하며 (k-1)번 pop을 하면
그 다음 값인 heap[0]가 찾아야하는 k(i//3 + 1)번째로 작은 값이 된다. 이 값을 m[i]에 저장하고 이 반복문을 리스트 A의 원소 개수만큼 반복한다.

for문이 n번 돌기 때문에 O(n)의 시간이 걸리고, heapify는 O(logn)이므로 O(n*logn)의 시간복잡도를 갖는다.
heapq.heappop 연산은 min 값을 pop하고 A[n-1]번째 노드를 루트에 배치시킨 후 다시 힙 속성을 만족할 때까지 연산을 반복한다. 이 때 heap은 완전 이진 트리로 구현되었기 때문에 부모 노드와 자식 노드가 한 level씩 내려갈 떄마다 비교 대상이 절반씩 감소하므로 O(logn)의 시간복잡도를 갖는다. (k-1)번 반복하여 수행되기 떄문에 최대 O(klogn)의 시간이 소요된다.

따라서 전체 코드의 시간복잡도는 n * (logn + k*logn + k) = n * ((k+1)logn + k) 이고 k는 상수로 가정하고 있으므로 시간복잡도는 O(nlogn)이다.
'''