# 스도쿠

def solve(A):
	 # 각 행, 열, 박스에서 사용된 숫자를 나타내는 보조 배열 생성 및 초기화
	used_in_row = [[False]*10 for _ in range(9)]
	used_in_col = [[False]*10 for _ in range(9)]
	used_in_box = [[False]*10 for _ in range(9)]

	for i in range(9):
		for j in range(9):
			# 셀이 비어있지 않다면 해당 숫자를 가져와서 used로 표시
			if A[i][j] != 0:
				num = A[i][j]
				used_in_row[i][num] = True
				used_in_col[j][num] = True
				used_in_box[i//3*3 + j//3][num] = True
	
	# 주어진 셀에 숫자가 안전하게 들어갈 수 있는지를 판단
	def is_safe(i, j, num):
		# 현재 숫자가 사용되지 않았으면 True
		return not (used_in_row[i][num] or used_in_col[j][num] or used_in_box[i//3*3 + j//3][num])

	def helper(i, j):
		if i == 9:
			return True
		ni, nj = (i, j+1) if j != 8 else (i+1, 0)
		if A[i][j] != 0:
			return helper(ni, nj)

		for num in range(1, 10):
			if is_safe(i, j, num):	# safe 이면 숫자 배치하고 used로 표시
				A[i][j] = num
				used_in_row[i][num] = True
				used_in_col[j][num] = True
				used_in_box[i//3*3 + j//3][num] = True
				if helper(ni, nj):
					return True
				A[i][j] = 0		# 해결하지 못했으면 셀 비우고 unused로 표시
				used_in_row[i][num] = False
				used_in_col[j][num] = False
				used_in_box[i//3*3 + j//3][num] = False
				
		# 모든 숫자를 시도했으나, 현재 셀에 안전하게 배치할 수 있는 숫자가 없다면 False 반환
		return False

	return helper(0, 0)

def check_sudoku(A):
	# check rows
	for i in range(9):
		B = A[i][:]
		B.sort()
		s = ''.join(str(x) for x in B)
		if s != '123456789':
			return False
	# check columns
	for j in range(9):
		B = []
		for i in range(9):
			B.append(A[i][j])
		B.sort()
		s = ''.join(str(x) for x in B)
		if s != '123456789':
			return False
	# check boxes
	for i in range(3):
		for j in range(3):
			B = []
			for a in range(3):
				for b in range(3):
					B.append(A[3*i+a][3*j+b])
			B.sort()
			s = ''.join(str(x) for x in B)
			if s != '123456789':
				return False
	return True 

A = [0]*9
for i in range(9):
	row = [int(x) for x in input()]
	A[i] = row

solve(A)
print(check_sudoku(A))