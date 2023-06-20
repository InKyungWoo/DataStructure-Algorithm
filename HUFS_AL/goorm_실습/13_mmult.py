# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

def matrix_mult():
    for j in range(1, n):
    	for i in range(j - 1, -1, -1):
            C[i][j] = math.inf # math module에서 제공하는 매우 큰 정수
            for k in range(i, j):
                cost = C[i][k] + C[k + 1][j] + P[i - 1] * P[k] * P[j]
                if cost <= C[i][j]:		# min update
                    C[i][j] = cost
    return C[0][n-1]

n = int(input()) # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
P = [int(x) for x in input().split()] # M_i = p_i x p_{i+1}
C = [[0]*n for _ in range(n)] # 비용을 저장할 2차원 리스트 C 초기화
min_cost = matrix_mult()
print(min_cost)

'''
- 첫 번째 for 루프는 j의 값을 변경하며, i와 j 사이에 있는 모든 행렬들에 대해 행렬 곱셈의 최소 연산 횟수를 계산한다.
- 두 번째 for 루프는 j에서 거꾸로 이동하며, i의 값을 감소시킨다. i는 항상 j보다 작거나 같으므로, 이 루프는 오른쪽 위 대각선 방향으로 행렬을 채운다.
- 세 번째 for 루프는 i와 j 사이의 모든 행렬들에 대해, 그 행렬을 기준으로 행렬 곱셈을 분할하여 최소 연산 횟수를 계산한다. 이를 위해 cost 변수에 행렬 i에서 k까지, 그리고 k+1에서 j까지의 최소 연산 횟수를 더하고, 이에 i-1번 행렬의 행의 수, k번 행렬의 열의 수, j번 행렬의 열의 수를 곱한다.
- if cost <= C[i][j]: C[i][j] = cost 로직을 통해 현재 계산된 비용이 이전에 저장된 비용보다 작거나 같은 경우, 해당 비용으로 업데이트한다.
- 결과적으로 C[0][n-1]에 저장된 값이 주어진 행렬들을 곱하는데 필요한 최소 연산 횟수가 된다.

전체 수행 시간은 O(n^3)
'''