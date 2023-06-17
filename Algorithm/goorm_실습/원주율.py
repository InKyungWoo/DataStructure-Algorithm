def long_add(A, B, C):
	 # 세 배열 A, B, C에서, C = A + B
	carry = 0		# 올림수 저장
	for i in range(len(A)-1, -1, -1):
		temp = A[i] + B[i] + carry
		carry = temp // 10000		# 10000으로 나눈 몫을 다음 자릿수의 carry로 설정
		C[i] = temp % 10000			# 10000으로 나눈 나머지를 C의 해당 자릿수에 저장

def long_sub(A, B, C):
	 # 세 배열 A, B, C에서, C = A - B
	borrow = 0		# 빌림수 저장
	for i in range(len(A)-1, -1, -1):
		temp = A[i] - B[i] - borrow		# A와 B의 해당 자릿수와 borrow 빼기
		# 만약 결과가 음수라면 10000을 더하고 borrow를 1로 설정
		if temp < 0:
			temp += 10000
			borrow = 1
		# 그렇지 않다면 borrow를 0으로 설정
		else:
			borrow = 0
		C[i] = temp

def long_div(A, b, C):
	# 배열 A를 정수 b로 나누어 배열 C에 저장, C = A/b
	remainder = 0		# 이전 계산의 나머지
	for i in range(len(A)):
		temp = A[i] + remainder * 10000
		C[i] = temp // b
		remainder = temp % b		# temp를 b로 나눈 나머지를 다음 계산을 위해 remainder에 저장

P = int(input("Precision = "))		# 계산하고자 하는 원주율의 소수점 이하 자리수를 입력 받음
L = P//4 + 2		# 배열의 크기 계산. 원주율의 각 숫자를 4자리 단위로 배열에 저장하기 위함
K = int(P/1.39894)+1		# Machin 공식에 따른 항의 개수를 계산
w, v, q, pi = [0]*L, [0]*L, [0]*L, [0]*L		# 배열들 초기화
w[0] = 16*5
v[0] = 4*239
for n in range(1, K+1):
  long_div(w, 5*5, w)
  long_div(v, 239*239, v)
  long_sub(w, v, q)
  long_div(q, 2*n-1, q)		# q를 2n-1로 나눈 결과를 다시 q에 저장
  if n%2 == 1: long_add(pi, q, pi)		# n이 홀수라면 pi에 q를 더하고,
  else: long_sub(pi, q, pi)						# n이 짝수라면 pi에서 q를 빼서 pi를 업데이트

# print pi value in proper format
output = str(pi[0]) + "."		# 원주율이 정수부 출력
for i in range(1, len(pi)):
    output += str(pi[i]).zfill(4)  #  원주율의 소수 부분을 4자리 단위로 출력. 필요시 앞에 0을 추가
print(output[:P+2])
