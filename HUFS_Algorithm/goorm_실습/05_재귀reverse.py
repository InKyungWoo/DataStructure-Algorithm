# 재귀 호출

def reverse(L, a):
	n = len(L)
	if a < n//2 :
		L[a], L[n-1-a] = L[n-1-a], L[a]
		reverse(L, a+1)   # 재귀 호출

A = list(input()) # 문자열을 입력받아 리스트로 변환
reverse(A)
print(''.join(str(x) for x in A))