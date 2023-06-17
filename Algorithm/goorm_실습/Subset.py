def print_subset(x):
	print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
	current_sum = sum(A[i]*x[i] for i in range(k))
	if k == len(A):
		return
	else:
		# code for x[k] = 1 and x[k] = 0
		if current_sum + A[k] <= S:
			# x[k] = 1
			x[k] = 1
			if current_sum + A[k] == S:	# solution is found
				print_subset(x)
			else:
				subset_sum(k+1)	
		# x[k] = o
		x[k] = 0
		subset_sum(k+1)
				
		
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
subset_sum(0)