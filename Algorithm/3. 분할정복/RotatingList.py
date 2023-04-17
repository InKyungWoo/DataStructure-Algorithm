# 이진탐색으로 시간복잡도 O(n) -> O(logn) 으로 줄일 수 있음

def find_smallest_index(A, start, end):
	if start == end: 			# 시작 인덱스와 마지막 인덱스가 같을 때
		return start 	
		
	mid = (start + end) // 2 		# mid 값을 이용해 분할정복
		
	if A[mid] < A[end]: 
		return find_smallest_index(A, start, mid) 	# 왼쪽 구간에 최소값이 있을 경우
	else:
		return find_smallest_index(A, mid + 1, end) 	# 오른쪽 구간에 최소값이 있을 경우

A = A = [int(x) for x in input().split()]

# 회전 횟수 = 리스트의 길이 - 최소값의 인덱스
k = len(A) - find_smallest_index(A, 0, len(A)-1)

# 회전을 하지 않은 경우
if len(A) == k: 	# 최소값의 인덱스가 0이면
   k = 0		# 회전횟수 0
		
print(k)

'''
1. 코드 설명

이 코드는 오름차순 정렬된 리스트 A의 회전 횟수를 구하는 코드이다. 함수 find_smallest_index()는 리스트 A와 시작점 start, 끝점 end를 인자로 받아 최소값의 인덱스를 찾는다.
그리고 리스트는 왼쪽으로만 회전한다고 가정하고 있으므로 '회전 횟수 k = 리스트A의 길이 - 최소값의 인덱스' 로 나타낼 수 있다.

- start와 end가 같다면 첫 번째 값 출력 (리스트 A가 이미 오름차순으로 정렬되어 있거나, 하나의 값으로 이루어져 있는 경우)
그리고 이진탐색을 위해 mid에 중간 인덱스 값을 저장한다.
- mid가 end보다 작다면 A[0] 부터 A[mid-1]까지는 회전되지 않은 상태이므로 리스트의 왼쪽 구간에서 다시 재귀적으로 탐색한다.
- mid가 end보다 크다면 A[mid+1] 부터 A[end] 사이에 회전이 일어났으므로 리스트의 오른쪽 구간에서 재귀적으로 최소 인덱스를 찾는다.
찾은 인덱스 값을 전체 길이에서 빼면 회전횟수 k를 구할 수 있다. 이 때 만약 리스트의 길이가 k와 같다면 최소값의 인덱스가 0이라는 의미로 이미 오름차순으로 정렬이 되어있다는 뜻이다. 따라서 k = 0 으로 출력한다.


2. 비교 횟수, 수행시간 분석

리스트를 반씩 나누어 이진탐색을 진행하므로 최악의 경우는 마지막 1개가 남을 때까지 찾는 경우이다. 연산횟수를 다음과 같이 정의한다면 전체 비교 회수는 T(n) = k + 1 이 된다.
- n개의 데이터가 1이 될 때 까지 2로 나누기 = k번
- 마지막 1개의 값에 대해 비교 연산 실행 = 1번

이 때 n이 1이 될 때 까지 k번 나눈 것이 worst case 이므로 n * (1/2^k) = 1 이고 이 식을 정리하면 n = 2^k 이다.
양 변에 log2를 취하면 k = logn이 되므로 시간복잡도는 T(n) = logn + 1 이다.
이를 Big-O 로 나타내면 O(logn)이 된다.
'''
