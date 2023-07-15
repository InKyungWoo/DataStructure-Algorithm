# 위상 정렬

# 테케 3~10 싹 다 에러..몰라 쉬벌
from collections import deque
import heapq

def TopologicalSort(n, m, edges):
    # n: 노드 수, m: 에지 수, edges: 에지 정보
    indegree = [0] * n # 진입 차수를 저장하기 위한 리스트
    graph = [[] for _ in range(n)] # 각 노드에 연결된 간선 정보를 담기 위한 인접 리스트 초기화

    # 간선 정보를 이용하여 그래프를 만듭니다.
    for a, b in edges:
        graph[a].append(b) # a에서 b로 이동 가능
        indegree[b] += 1 # 진입 차수를 1 증가

    # 위상 정렬 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = [] # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(n):
        if indegree[i] == 0:
            heapq.heappush(q, i) # 우선순위 큐를 사용하여 노드 번호가 작은 것 부터 처리

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = heapq.heappop(q)
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                heapq.heappush(q, i)

    # 위상 정렬 결과를 출력합니다.
    print(' '.join(map(str, result)))

n = int(input()) # 노드의 수 입력
m = int(input()) # 에지의 수 입력
edges = [] # 에지 정보를 담을 리스트

for _ in range(m):
    a, b = map(int, input().split()) # 간선 정보 입력
    edges.append((a, b))

TopologicalSort(n, m, edges)

'''
우선순위 큐를 사용한 위상 정렬(Topological Sort) 알고리즘을 구현한 코드로 n개의 정점과 m개의 간선이 주어진 방향 그래프에서 위상 정렬의 순서를 찾는다.
위상 정렬 알고리즘은 매번 진입 차수가 0인 노드를 우선순위 큐에 추가하여 노드 번호가 작은 순서대로 처리하고, 큐에서 하나씩 꺼낸 뒤 해당 노드가 가리키는 노드의 진입 차수를 1씩 감소시켜, 노드의 진입 차수가 0이 되면 다시 큐에 삽입하고 수행을 반복한다.

수행 시간 분석:
1. 그래프 초기화: O(m) (m은 간선의 수)
2. 위상 정렬 알고리즘 수행: 모든 노드와 간선에 대해 반복하며, 각 노드에 대해 우선순위 큐(push/pop)를 사용하므로 O(n log n + m log n) (n은 노드의 수)
따라서, 이 알고리즘의 전체 수행 시간의 Big-O 표기는 O(nlog n + mlogn)이다.
'''
