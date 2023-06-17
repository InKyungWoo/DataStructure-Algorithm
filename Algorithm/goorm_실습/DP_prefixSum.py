def max_prefix(A):
	n = len(A)
	dp = [0] * n  # dp[i]: A[0]부터 A[i]까지의 연속된 부분 수열의 합의 최대값
	dp[0], max_sum = A[0], dp[0]  # 초기화
	
	for i in range(1, n):
		dp[i] = max(A[i], dp[i-1] + A[i])  # 현재 원소를 포함한 경우와 이전 연속 부분 수열의 합과 현재 원소를 합한 경우 중 큰 값 선택
		max_sum = max(max_sum, dp[i])  # max 업데이트
	return max_sum

n = int(input())  # 정수 개수 입력
A = [int(x) for x in input().split()]  # n개의 정수를 입력받아 리스트 A에 저장

print(max_prefix(A))