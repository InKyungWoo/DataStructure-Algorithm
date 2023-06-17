def QuickSelect(L, k):
	if len(L) == 0:
		return None
	
	pivot = L[0]  # pivot을 L의 첫 번째 값으로 설정
	Left, Mid, Right = [], [], []
	Mid.append(pivot)

	for i, x in enumerate(L):
		if i == 0:  # 첫 번째 요소는 피벗으로 이미 Mid 리스트에 추가되었으므로 건너뜁니다
			continue
		if x == pivot: Mid.append(x)
		elif x < pivot: Left.append(x)
		else: Right.append(x)

	if len(Left) >= k:
		return QuickSelect(Left, k)
	elif len(Left) + len(Mid) < k:
		return QuickSelect(Right, k - len(Left) - len(Mid))
	else:
		return pivot

n, k = map(int, input().split())  # 첫 줄에서 정수 개수 n과 k를 입력받음
L = [int(x) for x in input().split()] 
print(QuickSelect(L, k))
