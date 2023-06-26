import time, random

def prefixSum1(X):
	for i in range(0, len(X)):
		S = []
		sum = 0
		for j in range(0, i+1):
			sum += X[j]
			S.append(sum)
	return S

def prefixSum2(X):
	S = X
	for i in range(1, len(X)):
		S[i] = S[i-1] + X[i]
	return S
	
random.seed()			# random 함수 초기화
n = int(input())	# n 입력받음

# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X = []
for i in range(n):
	num = random.randint(-999, 999)
	if num not in X:
		X.append(num)
#print("X : ", X)
#print(prefixSum1(X))
#rint(prefixSum2(X))

# 두 함수의 수행시간 출력
before = time.process_time()
prefixSum1(X) # prefixSum1 호출
after = time.process_time()
print("process time1 : ",after - before)
#print("prefixSum1 : ", prefixSum1(X, n))		

before = time.process_time()
prefixSum2(X) # prefixSum2 호출
after = time.process_time()
print("process time2 : ", after - before)
#print("prefixSum2 : ", prefixSum2(X, n))		# 확인용
