# 3등분 합병 정렬

def merge(A, first, m1, m2, last):
	temp = []		# 합병할 리스트를 임시로 저장할 리스트
	i, j, k = first, m1+1, m2+1		# 각 구간의 시작 인덱스

	# 세 리스트 모두 비어있지 않을 떄	
	while i <= m1 and j <= m2 and k <= last:
		if A[i] < A[j]:		# 첫번째 리스트의 원소가 가장 작을 때
			if A[i] < A[k]:
				temp.append(A[i])
				i += 1
			else:		# 세 번째 리스트의 원소가 가장 작을 때
				temp.append(A[k])
				k += 1
		else:			# 두 번째 리ㅡ트의 원소가 가장 작을 때
			if A[j] < A[k]:
				temp.append(A[j])
				j += 1
			else:		# 세 번째 리스트의 원소가 가장 작을 때
				temp.append(A[k])
				k += 1
	
	# 첫번쨰 & 두번쨰 리스트
	while i <= m1 and j <= m2:
		if A[i] < A[j]:
			temp.append(A[i])
			i += 1
		else:
			temp.append(A[j])
			j += 1
	
	# 첫번쨰 & 세번째 리스트
	while i <= m1 and k <= last:
		if A[i] < A[k]:
			temp.append(A[i])
			i += 1
		else:
			temp.append(A[k])
			k += 1
	
	# 두번째 & 세번째 리스트
	while j <= m2 and k <= last:
		if A[j] < A[k]:
			temp.append(A[j])
			j += 1
		else:
			temp.append(A[k])
			k += 1
	
	while i <= m1:
		temp.append(A[i])
		i += 1
	while j <= m2:
		temp.append(A[j])
		j += 1
	while k <= last:
		temp.append(A[k])
		k += 1
	
	# 임시 리스트의 값 복사
	for i in range(first, last+1):
		A[i] = temp[i-first]

def m_sort(A, first, last):
	if first < last:
		m1 = first + (last-first) // 3
		m2 = first + 2 * (last-first) // 3
		m_sort(A, first, m1)	# 각 구간에 대해 재귀적으로 정렬
		m_sort(A, m1+1, m2)
		m_sort(A, m2+1, last)
		merge(A, first, m1, m2, last)

def check(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:  # 정렬이 제대로 되어있지 않다면 False 반환
            return False
    # 리스트의 첫 번째 원소, 중간 원소, 마지막 원소의 합 반환
    return A[0]+A[len(A)//2] +A[-1]

A = [int(x) for x in input().split()]
m_sort(A, 0, len(A)-1)
print(check(A))