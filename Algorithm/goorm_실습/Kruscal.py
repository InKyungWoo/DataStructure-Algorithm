class DisjointSet:
	def __init__(self, n):
		self.parent = list(range(n))  # 각 노드의 부모 노드 정보를 저장. 초기에는 자기 자신이 부모
		self.rank = [0]*n  # 루트 노드가 속한 트리의 랭크(높이)

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])  # 경로 압축. x의 최상위 부모를 찾아서 x의 부모로 직접 연결
		return self.parent[x]  # x의 최상위 부모 반환

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
	edges = [(w, u, v) for u in range(n) for v, w in G[u]]	# 모든 간선 정보를 (가중치, 시작노드, 도착노드) 형태로 변환
	edges.sort()		# 가중치 기준으로 간선들을 정렬

	ds = DisjointSet(n)
	mst_weight = 0
	# 가중치가 작은 간선부터 순회
	for weight, u, v in edges:
		# 사이클을 생성하지 않는 경우 MST의 총 가중치에 더해줌
		if ds.find(u) != ds.find(v):
			mst_weight += weight
			ds.union(u, v)
	return mst_weight

n = int(input())		# 노드의 수 입력
m = int(input())		# 에지의 수 입력
G = [[] for _ in range(n)]		# 그래프 초기화

for _ in range(m):
	u, v, w = map(int, input().split())
	G[u].append((v, w))
	G[v].append((u, w))

print(Kruskal(G))

'''
Kruskal 알고리즘을 사용하여 최소 신장 트리의 가중치 합을 구하고자 한다. 각 간선을 가중치 기준으로 정렬한 뒤, 분리 집합(Disjoint set)을 사용하여 사이클을 생성하지 않는 간선만 MST에 추가하는 방식으로 이를 위해 DisjointSet 클래스에서 union과 find 연산이 수행됩니다.

자료구조:
1. DisjointSet: 분리 집합(Disjoint set)을 나타내는 클래스로, 서로 중복되지 않은 원소들의 집합을 표현하는 데 사용되며 두 가지 리스트가 있다.
   - parent: 각 노드의 부모 노드 정보를 저장한다. (초기에는 모든 노드의 부모가 자기 자신)
   - rank: 루트 노드가 속한 트리의 높이(rank)를 저장한다.
2. Graph: 각 노드에 대한 인접 리스트로 구성된다.

수행시간 분석:
1. 분리 집합(Disjoint set)의 find 연산: 최악의 경우 시간 복잡도는 O(log V)이다 (V는 노드 수)
2. 분리 집합(Disjoint set)의 union 연산: 최악의 경우 시간 복잡도는 O(log V)이다 
3. 간선을 정렬하는 과정: 파이썬의 내장 sort 함수를 사용하면 최악의 경우 시간 O(E*log E)이 걸린다 (E는 간선 수).

전체적인 시간 복잡도는 간선 정렬(O(E*log E))에 분리 집합의 find 및 union 연산(O(E * log V))이 합산되어 O(E * log E + E * log V)이다. V-1개의 간선이 선택되면서 분리 집합 연산이 수행되므로, 보통 O(E*log E)로 일반화하여 표현한다.
'''
