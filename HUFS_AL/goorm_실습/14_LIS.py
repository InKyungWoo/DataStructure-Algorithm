def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]: 
            print(seq[i], end="")
        else:
            print("_", end="")
    print()

def LIS_DP(seq):    # code here
	n = len(seq)			# seq의 길이
	dp = [1] * n			# dp 배열 초기화 (모든 원소를 1로 설정)
	index = [-1] * n	# 부분 문자열을 저장하기 위한 리스트
	
	# LIS를 계산
	for i in range(1, n):
		for j in range(i):
			if seq[i] > seq[j] and dp[i] < dp[j] + 1:
				dp[i] = dp[j] + 1
				index[i] = j

	# LIS의 최대 길이를 찾아 그 위치를 저장
	max_length = max(dp)
	max_index = dp.index(max_length)

	# LIS의 인덱스를 저장할 리스트
	seq_index = [0] * max_length
	seq_index[-1] = max_index

	# 인덱스 리스트를 업데이트
	for i in range(max_length-2, -1, -1):
		seq_index[i] = index[seq_index[i+1]]

	# 가장 긴 증가하는 부분 수열의 인덱스를 True로 표시하는 리스트를 생성
	x = [0] * n
	for i in seq_index:
		x[i] = 1

	return max_length, x

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print(lis)