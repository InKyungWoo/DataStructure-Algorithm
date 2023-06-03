# for문 사용, 불필요한 연산 줄인 코드
# 최종 제출하고 만점받은 코드

def max_sum(A, left, right):
    
    # 리스트의 길이가 1인 경우
    if left == right: return A[left]

    m = (left + right) // 2

    # 1. left에 최대구간이 있는 경우 : (T(2/n))
    case_1 = max_sum(A, left, m)

    # 2. right에 최대구간이 있는 경우 : (T(2/n))
    case_2 = max_sum(A, m + 1, right)

    # 3. 걸쳐져 있는 경우 (왼쪽 최대구간 + 오른쪽 최대 구간) : for루프 각각 시간복잡도 O(n)
    sum_L = 0
    max_L = -100000000
    for i in range(m, left-1, -1):
        sum_L += A[i]
        max_L = max(max_L, sum_L)

    sum_R = 0
    max_R = -100000000
    for j in range(m + 1, right+1):
        sum_R += A[j]
        max_R = max(max_R, sum_R)

    case_3 = max_L + max_R

    return max(case_3, max(case_1, case_2))

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)

'''
1. 알고리즘 설명

이 코드는 분할정복 알고리즘을 사용하여 최대 구간 합을 찾는 함수 max_sum을 정의하고 그 값을 출력하는 코드이다.
우선 n개의 정수를 입력받아 리스트 A에 저장하고, 시작 인덱스인 left와 끝 인덱스인 right를 인자로 받는다.

- 리스트의 길이가 1인 경우 해당 요소를 반환하고, 리스트를 반으로 나눈 중간 인덱스 m을 구한다.
- 최대구간이 왼쪽 반 또는 오른쪽 반 구간에 존재하는 경우는 재귀적으로 함수를 호출하여 최대 구간 합을 구하고, 둘 중 큰 값이 반환된다.
- 최대구간이 양쪽에 걸쳐있는 경우, 반복적으로 left부터 m까지의 요소들의 합과 m+1부터 right까지의 요소들의 합을 각각 계산하고, 임의로 설정한 음수 max_L(R)과 비교 및 업데이트 하며 최대 합을 찾는다.
- 최종적으로 찾은 3개의 값 중 가장 큰 값이 반환된다.


2. 수행시간

이 코드의 점화식 T(n)을 구하면 case_1과 case_2에서 입력받은 리스트를 반으로 나누어 수행하므로 각각 T(2/n)이다. 그리고 case3에서는 for문이 각각 n번씩 실행되므로 2*n이다.
따라서 기본 연산을 제외한 전체 점화식은 T(n) = 2*T(n/2) + 2n 이고 편의를 위해 T(n) = 2T(n/2) + cn으로 간략하게 나타낼 수 있다. 
이를 전개하여 계산하면 다음과 같다.

T(n) = 2T(n/2) + cn
		 = 2(2T(n/2^2)+cn/2) + cn = 4T(n/4)+ 2cn
		 = 4(2T(n/8) + cn/4) + 2cn = 8T(n/8) + 3cn
		 = 8(2T(n/16) + cn/8) + 3cn = 16T(n/16) + 4cn
		 = ...
		 = 2^k T(n/2^k) + kcn
이 때 2^k = n 이므로 양변에 log2를 취하면 k = logn이다. 이를 위 식에 대입하여 정리하면
		 = n * T(n/n) + logn * cn
		 = n * T(1) + c * nlogn 이고 T(1)과 c는 상수이므로 Big-O로 나타내면 최종 수행시간은 O(nlogn)이 된다.
'''