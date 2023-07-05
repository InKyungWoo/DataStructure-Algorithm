# 힙 구성과 정렬 실습

class Heap:
	def __init__(self, L=[]):
		self.A = L
		self.make_heap()
	def __str__(self):
		return str(self.A)

	def heapify_down(self, k, n):
		while 2*k+1 < n: 
			L, R = 2*k + 1, 2*k + 2 
			if L < n and self.A[L] > self.A[k]: 
				m = L 
			else: 
				m = k 
			if R < n and self.A[R] > self.A[m]: 
				m = R 
			if m != k: 
				self.A[k], self.A[m] = self.A[m], self.A[k] 
				k = m
			else:
				break

	def make_heap(self):
		n = len(self.A)
		for k in range(n-1, -1, -1): 
			self.heapify_down(k, n)
	
	def heap_sort(self):
		n = len(self.A)
		for k in range(len(self.A)-1, -1, -1): 
			self.A[0], self.A[k] = self.A[k], self.A[0] 
			n = n - 1
			self.heapify_down(0, n) 

L = [int(x) for x in input().split()]
H = Heap(L)
H.heap_sort()
print(H)

'''
- heapify_down(self, k, n) : 인덱스 k에서 시작하여 재귀적으로 작동하며, 자식 노드 중 값이 더 큰 노드와 부모 노드를 교환하는 과정을 반복하여 하향식으로 힙을 정렬한다.

- make_heap(self) : 배열의 중간부터 시작하여 역순으로 heapify_down 함수를 호출함으로써 배열 전체를 힙으로 변환한다.

- heap_sort(self) : 힙의 루트 노드(가장 큰 값)와 마지막 노드를 교환한 후, 마지막 노드를 제외하고 힙을 다시 정렬하는 과정을 반복한다.
'''
