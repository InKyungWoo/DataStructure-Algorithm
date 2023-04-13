# 다항식 계산 - 두 가지 버전(O(n^2), O(n)) 수행 시간 비교
import random, time

def evaluate_n2(A, x):
	# code for O(n^2)-time function
  sum_val = 0
  for i in range(n):
    square = 1
    # x의 제곱승 값 구하기, i=0일때는 j in range(0)이므로 실행하지 않음 -> square = 1
    for j in range(i):
      square *= x
    # A[i]의 요소와 위에서 구한 제곱승값 각각 곱해서 sum_val에 합산
    sum_val += A[i] * square
  return sum_val

def evaluate_n(A, x):
	# code for O(n)-time function
  sum_val = 0
  square = x
  # A[1] 부터 x의 i제곱 만큼 곱하기
  for i in range(1,n):
    A[i] = A[i] * square
    square *= x           # x의 i+1 제곱 계산 (다음 제곱값)
  #print(A) # -> 계산된 리스트 A 확인
  for i in range(n):
    sum_val += A[i]
  return sum_val


random.seed()		# random 함수 초기화

# n 입력받음
n = int(input())

# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = [random.randint(-1000,1000) for i in range(n)]

# x값은 randint(-1000,1000)을 호출하여 생성함
x = 100

print("입력 크기 n: ", n)
#print("list A: ", A)
print("randint x: ", x)

# evaluate_n2 호출
s_n2 = time.process_time()
evaluate_n2(A, x)
e_n2 = time.process_time()
#print("evaluate_n2 의 실행 결과: ", evaluate_n2(A, x))

# evaluate_n 호출
s_n = time.process_time()
evaluate_n(A, x)
e_n = time.process_time()
#print("evaluate_n 의 실행 결과: ", evaluate_n(A, x))

# 두 함수의 수행시간 출력
print('evaluate_n2 의 수행시간: ', e_n2 - s_n2)
print('evaluate_n 의 수행시간: ', e_n - s_n)