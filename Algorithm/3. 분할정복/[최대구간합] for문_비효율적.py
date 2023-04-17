# 1~10번 중 9번 테케 fail, 더 오래걸림

def max_sum(A, left, right):
	if left == right: 
		return A[left]

	m = (left + right) // 2			# 중간값

	# 1. 최대 합이 왼쪽에 존재하는 경우 
	R = max_sum(A, left, m)
	
	#2. 오른쪽에 존재하는 경우
	L = max_sum(A, m+1, right)

	result = max(R,L)			# 둘 중 큰값을 result에 저장
	
	# 3. 양쪽에 걸치는 경우 (최대 합 = 왼쪽 끝 + 오른쪽 시작부분의 합)
	sum_L = 0; max_L = -10000000000; sum_R = 0; max_R = -10000000000; 		# 초기화
	for i in range(m, 0, -1):
		sum_L += A[i] 
		max_L = max(max_L, sum_L) 

	for i in range(m+1, right+1):
		sum_R += A[i]
		max_R = max(max_R, sum_R) 
	
	both = max_L + max_R

	return max(result, both)			# 둘 중 큰값


A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)


'''
이 코드의 시간 복잡도는 일반적인 분할 정복 알고리즘과 같이 O(nlogn)이다. 
입력받은 배열을 둘로 쪼개고, 재귀적으로 호출하면서 최대 합을 구하는 부분에서 O(logn)의 시간이 소요되고, 
두 부분을 걸쳐서 최대 합을 구하는 부분에서 O(n)의 시간이 소요되기 때문입니다.
각 부분에서 최대 부분 합을 구하기 위해 반복문을 사용하고 있는데 이 경우 각 부분의 시간 복잡도는 O(n)이다. 
따라서 전체 알고리즘의 시간 복잡도는 O(nlogn) * O(n) = O(n^2 logn)이므로 큰 입력에 대해서는 비효율적일 수 있다.
'''