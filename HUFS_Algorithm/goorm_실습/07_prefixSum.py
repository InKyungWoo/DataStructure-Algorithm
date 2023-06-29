# 분할정복 최대 구간 합

def prefixSum(A):
	max_sum = float('-inf')		# 음수로 초기화

	for i in range(len(A)):
		curr_sum = 0
		for j in range(i, len(A)):
			curr_sum += A[j]
			max_sum = max(max_sum, curr_sum)  # 둘 중 큰 값 저장

	return max_sum

A = [int(x) for x in input().split()]  # n개의 정수를 입력받아 리스트 A에 저장
print(prefixSum(A))
