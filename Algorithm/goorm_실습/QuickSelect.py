def QuickSelect(L, k):
	p = L[0]
	Left, Mid, Right = [], [], []
	for x in L:
		if x < p: Left.append(x)
		elif x > p: Right.append(x)
		else: Mid.append(x)
	
	if len(Left) >= k:
		return QuickSelect(Left, k)
	elif len(Left) + len(Mid) < k:
		return QuickSelect(L, k - len(Left) - len(Mid))
	else:
		return p

n, k = map(int, input().split())  # 첫 줄에서 정수 개수 n과 k를 입력받음
L = [int(x) for x in input().split()] 
print(QuickSelect(L,k))