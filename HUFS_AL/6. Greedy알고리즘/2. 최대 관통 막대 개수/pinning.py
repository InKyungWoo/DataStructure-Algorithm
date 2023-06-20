# 못 하나로 관통할 수 있는 막대의 최대 개수 구하기

import heapq

n = int(input())
L = []
for _ in range(n):
	a, b = map(int, input().split())
	L.append([a, b])
L.sort(key=lambda x : [x[0], x[1]]) 	# a기준 오름차순 정렬 후 b기준으로 오름차순 정렬 => O(nlogn)

F = []		# 끝나는 점 모음

heapq.heappush(F, L[0][1])
cnt = 1 
for i in range(1, n):
	if F[0] < L[i][0]:
		heapq.heappop(F)
	heapq.heappush(F, L[i][1])
	cnt = max(cnt, len(F))
print(cnt)

'''
1. 알고리즘 분석
1) 막대의 시작점을 기준으로 오름차순 정렬 후, 끝점을 기준으로 오름차순 정렬한다.
2) 첫 번째 막대의 끝점을 F에 저장한다.
3) 다음 막대부터 순차적으로 보면서,F에 저장된 끝점과 비교하여 겹치는지 확인한다.
	- 겹친다면, 새로운 못이 필요하므로 push 하고 끝점을 F에 저장한다.
	- 겹치지 않는다면, 이 막대는 기존 못에 꽂힐 수 있으므로 pop하고 끝점을 F에 저장한다.
이러한 과정을 모든 막대에 대해 반복하면 결과적으로 cnt에는 최대로 겹치는 막대의 개수가 저장된다.

2. 수행시간 분석
- 입력: O(n)
- 정렬: O(nlogn)
- heap연산은 부모노드와 자식노드의 비교 및 swap을 통해 한 level씩 내려갈때 마다 비교 대상이 절반씩 감소하는 것이므로 O(logn)의 수행시간이 걸린다.
	반복문 내에서 n번 반복하며 수행하므로 3)의 수행시간은 O(nlogn)이다.  
따라서 전체 시간복잡도는 O(nlogn)이다.
'''