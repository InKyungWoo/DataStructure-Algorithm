def reverse(A):
	n, i = len(A), 0
	while i < n//2 : # 절반까지
		A[i], A[n-1-i] = A[n-1-i], A[i]
		i += 1

A = list(input()) # 문자열을 입력받아 리스트로 변환
reverse(A)
print(''.join(str(x) for x in A))