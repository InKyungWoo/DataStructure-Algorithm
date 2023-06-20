# while문 사용, 4,5번 테케 안되다가 범위 수정으로 해결!
def max_sum(A, left, right):
	# A[left], ..., A[right] 중 최대 구간 합 리턴
  if left == right:
      return A[left]

  m = (left + right) // 2
	
	# left에 최대구간
  R = max_sum(A, left, m)

  # right에 최대구간
  L = max_sum(A, m + 1, right)

  # 걸쳐져 있는 경우(왼쪽 최대구간 오른쪽 최대 구간 합)
  sum_left = 0
  i = m
  max_L = -100000000
  while (i >= left):
      sum_left += A[i]
      #max_L = max(sum_left, max_L, A[i])
      max_L = max(sum_left, max_L)
      i-=1

  sum_right = 0
  j = m + 1
  max_R = -100000000
  while (j <= right):
      sum_right += A[j]
      #max_R = max(sum_right, max_R, A[j])
      max_R = max(sum_right, max_R)
      j+=1
  M = max_L + max_R

  return max(M, max(R, L))


A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)

'''
걸쳐 있는 경우(3번)를 재귀적으로 해결하지 않고, while문을 활용하여 해결하면 코드 길이가 짧아지고 더 직관적일 수 있지만, 
while문 내에서 반복적인 연산이 이루어지기 때문에 시간 복잡도가 더 높아질 가능성이 있음. 그리고 예외 상황에서 코드가 동작하지 않을 수도 있다. 
예를 들어, 배열의 모든 원소 값이 음수일 때 while문이 한 번도 실행되지 않기 때문에 잘못된 값을 반환할 수 있음!

분할 정복의 특성상 재귀 호출이 수행될 때마다 전체 문제의 크기가 절반으로 줄어들기 때문에, 분할된 구간의 크기가 1일 때까지 문제를 분할한다.
각 분할 단계에서 비교 연산과 덧셈 연산을 수행하므로, 총 비교 연산과 덧셈 연산 수행 횟수는 각 단계에서 구간의 크기만큼 일어난다.
전체 구간의 크기가 n이라면, 분할 단계는 logn번 발생하며, 각 단계에서의 연산 횟수는 해당 단계의 구간의 크기만큼 발생한다.
따라서 총 수행 시간은 O(nlogn)이다.
'''