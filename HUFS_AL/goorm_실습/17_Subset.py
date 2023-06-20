def print_subset(x):
	print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
	global found_cnt
	current_sum = sum(A[i]*x[i] for i in range(k))
	if k == len(A):
		if current_sum == S:
			found_cnt += 1		# 추가될 때 마다 +1
			print_subset(x)
		if sum(x) == 0 and found_cnt == 0:		# 최종 합이 0, cnt도 0인 경우
			print([])
	else:
		# code for x[k] = 1 and x[k] = 0
		# 선택O
		if current_sum + A[k] <= S:
			x[k] = 1
			subset_sum(k+1)
		# 선택X
		x[k]=0
		subset_sum(k+1)

found_cnt = 0

A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
subset_sum(0)