# 프림 알고리즘

import heapq

class Prims:
	def __init__(self, vertex):
		self.vertex = vertex
		self.data = [[] for _ in range(self.vertex)]

	def AddAdges(self, src, dest, cost):
		if src == dest:
			print('same')
		else:
			self.data[src].append((dest, cost))
			self.data[dest].append((src, cost))

	def rasta(self, source):
		visited = [False] * self.vertex
		pq = [(0, source)]
		total_cost = 0

		while pq:
			cost, node = heapq.heappop(pq)
			if visited[node]:
				continue
			visited[node] = True
			total_cost += cost

			for neighbor, edge_cost in self.data[node]:
				if not visited[neighbor]:
					heapq.heappush(pq, (edge_cost, neighbor))

		print(total_cost)


n = int(input())
m = int(input())
g = Prims(n)
for _ in range(m):
	a, b, c = map(int, input().split())
	g.AddAdges(a, b, c)

g.rasta(3)

'''
이 코드는 Prim 알고리즘을 이용하여 최소 신장 트리의 가중치 합을 구하는 문제이다.

자료구조:
1. 각 노드에 대한 인접 리스트: `self.data`
2. 방문 여부를 확인하는 리스트: `visited`
3. 우선 순위 큐(priority queue, 지금의 코드에서는 `pq`)

시간 복잡도:
- 인접 리스트: 인접 리스트는 희소 그래프(sparse graph)에서 효율적이며 각 노드에 대해 연결된 노드와 가중치 정보를 저장한다. 인접 리스트를 구성하는 시간 복잡도는 O(E)로 나타낼 수 있다 (E는 엣지의 수).
- 방문 여부 확인: 방문 여부를 확인하기 위한 리스트는 각 노드에 대해 상수 시간에 접근이 가능해야 하므로 리스트 길이가 노드의 수만큼 있다. 따라서 공간 복잡도는 O(V)입니다 (V는 노드의 수).
- 우선 순위 큐(priority queue): Prim 알고리즘에서 가장 작은 가중치를 가진 간선을 찾는 과정에서 우선 순위 큐를 사용한다. Python에서는 heapq 모듈을 통해 이진 힙(binary heap)을 사용하여 구현하였고, 우선 순위 큐의 삽입과 삭제 작업은 각각 O(log E)의 시간 복잡도를 가진다.
- 모든 노드를 한 번씩 방문하고(반복문에서 최대 V번 수행), visited 리스트를 수정하고(상수 시간), heapq.heappush와 heapq.heappop 연산을 하므로 (O(log E)) 전반적인 시간 복잡도는 O((V + E) log E) 이다.
'''
