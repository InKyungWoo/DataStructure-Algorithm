import heapq

class DisjointSet:
	def __init__(self, n):
		self.parent = list(range(n))	# 각 노드의 부모 노드 정보를 저장. 초기에는 자기 자신이 부모
		self.rank = [0] * n						# 루트 노드가 속한 트리의 랭크(높이)
	
	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])	# 경로 압축. x의 최상위 부모를 찾아서 x의 부모로 직접 연결
		return self.parent[x]	 # x의 최상위 부모 반환

	def union(self, x, y):
		px, py = self.find(x), self.find(y)		# x와 y의 최상위 부모 찾기
		if self.rank[px] > self.rank[py]:			# 랭크가 더 큰 쪽이 부모가 됨
			self.parent[py] = px
		else:
			self.parent[px] = py
			if self.rank[px] == self.rank[py]:	# 랭크가 같을 경우 병합 후 랭크 증가
				self.rank[py] += 1

def Kruskal(G):
	n = len(G)
	edges = [(w, u, v) for u in range(n) for v, w in G[u]]
	heapq.heapify(edges)  # 간선들을 최소 힙으로 변환

	ds = DisjointSet(n)
	mst_weight = 0
	num_selected_edges = 0

	# 최소 가중치 간선이 선택되면서 순회
	while edges and num_selected_edges < n - 1:
		weight, u, v = heapq.heappop(edges)
		# 사이클을 생성하지 않는 경우 MST의 총 가중치에 더하기
		if ds.find(u) != ds.find(v):
			mst_weight += weight
			ds.union(u, v)
			num_selected_edges += 1

	return mst_weight

n = int(input())
m = int(input())
G = [[] for _ in range(n)]

for _ in range(m):
	u, v, w = map(int, input().split())
	G[u].append((v, w))			# (도착노드, 가중치) 형태로 인접 리스트에 연결 정보를 추가
	G[v].append((u, w))			# 양방향 그래프이므로 반대 방향도 추가

print(Kruskal(G))


'''
<자료구조>
1. `G`: 인접 리스트를 사용한 그래프 표현으로 각 노드에 연결된 에지 정보들이 리스트로 저장되어 있다.
2. `edges`: 모든 간선 정보를 포함한 최소 힙
3. `DisjointSet`: 공통 부모를 찾기 위한 서로소 집합(Disjoint Set)을 표현하는 클래스

<수행시간>
1. 그래프 초기화: 입력 크기에 비례하여 O(m) (m은 간선의 수)
2. Kruskal 알고리즘: 간선 리스트를 최소 힙으로 만드는 것은 O(m) 시간이 걸린다. 간선을 모두 처리하면서 사이클을 생성하지 않으면서 MST를 완성하는 과정은 크게 2가지 요소로 나뉜다:
   - heapq.heappop 연산은 O(log m) 시간이 걸리며, 최악의 경우 간선을 모두 검사해야 하므로 이 부분의 시간 복잡도는 O(m log m)
   - DisjointSet에서의 find와 union 연산은 모두 거의 상수시간에 가깝게 수행되므로 전체 시간 복잡도 또한 O(m log m)
따라서, 전체 수행 시간 O(nlogn)이며 간선의 수에 따라 로그 스케일로 증가한다.
'''
