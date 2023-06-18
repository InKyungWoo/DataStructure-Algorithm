# 9번 테케 timeout.....

def find_empty(A):
	# A에서 0인 셀(빈 칸)의 위치를 반환
	for i in range(9):
		for j in range(9):
			if A[i][j] == 0:
				return i, j
	return None, None		# 없으면 None

def is_safe(A, row, col, num):
	# 현재 행에서 같은 숫자가 있는지 확인
	if num in A[row]:
		return False
	# 현재 박스에 같은 숫자가 있는지 확인
	for i in range(9):
		if A[i][col] == num:
			return False

	start_row, start_col = row - row % 3, col - col % 3
	for i in range(3):
		for j in range(3):
			if A[i + start_row][j + start_col] == num:
				return False

	return True		# 없으면 True

def solve(A):
	# 빈칸 찾기
	row, col = find_empty(A)
	if row is None:		# 빈칸 없으면 풀린거임
		return True
	
	# 빈칸 있으면 1~9까지 넣으면서 풀기
	for num in range(1, 10):
		if is_safe(A, row, col, num):
			A[row][col] = num
			if solve(A):
				return True
			A[row][col] = 0
	
	# 1~9까지 다 넣어서 해봤는데도 안풀리면 False
	return False

	# 아래에 호출 및 main code는 동일...
