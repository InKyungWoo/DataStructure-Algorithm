# heapq 모듈로 우선순위 큐 사용하여 12번 테케 timeout 해결
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

# 12번 테케 - Timeout으로 Runtime Error
'''
class Prims:
	def __init__(self,vertex):
		self.vertex = vertex
		self.data = [[0 for i in range(self.vertex)] for j  in range(self.vertex)]

	def AddAdges(self,src,dest,cost):
		if src == dest:
			print('same')
		else:
			self.data[src][dest] = cost
			self.data[dest][src] = cost

		return self.data

	def GetNeighbour(self,vertex):
		a = []
		for i in range(len(self.data[vertex])):
			if self.data[vertex][i] > 0:
				a.append(i)
		return a

	def weight(self,src,dest):
		return self.data[src][dest]

	def rasta(self,source):
		visited = []
		dct = {i:999999 for i in range(len(self.data))}
		dct[source] = 0
		temp = {i: dct[i] for i in dct}

		while temp:
			minNode = 99999
			key = None
			for i in temp:
				if temp [i] < minNode:
					minNode = temp[i]
					key = i
			temp.pop(key)
			if key not in visited:
				visited.append(key)
				x = self.GetNeighbour(key)
				for j in x:
					if (self.weight(key,j)< dct[j]) and (j not in visited):
						dct[j] = self.weight(key,j)
						temp[j] = self.weight(key,j)
		print(sum(dct.values()))


n = int(input())
m = int(input())
g = Prims(n)
for i in range(m):
	(a, b, c) = tuple([int(x) for x in input().split()])
	g.AddAdges(a, b, c)

g.rasta(3)
'''