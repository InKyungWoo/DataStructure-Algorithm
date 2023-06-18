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
