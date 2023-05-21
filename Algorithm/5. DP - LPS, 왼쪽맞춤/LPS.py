# 최장 회문 부수열 (Longest Palindrome Subsequence)

def LPS(s):
	n = len(s)
	# 2차원 리스트 생성
	dp = [[0] * n for _ in range(n)]

	for i in range(n):
		dp[i][i] = 1  # 한 글자인 경우, 팰린드롬의 길이는 1
		
	# dp 테이블 채우기 
	for l in range(2, n + 1):    # 부분 문자열의 길이를 2부터 n까지 순회
		for i in range(n - l + 1):
			j = i + l - 1
			if s[i] == s[j]:   # i와 j의 문자가 같은 경우
				if l == 2:	     # 부분 문자열의 길이가 2인 경우
					dp[i][j] = 2
				else:
					dp[i][j] = dp[i+1][j-1] + 2    # 이전에 계산된 팰린드롬의 길이를 이용하여 값 계산
			else:
				dp[i][j] = max(dp[i+1][j], dp[i][j-1])   # 문자가 다른 경우, 인접한 부분 문자열 중 최댓값 선택

	return dp[0][n-1]    # 전체 문자열에서의 가장 긴 팰린드롬 부분 문자열의 길이 반환

word = input()
print(LPS(word))


'''
이 알고리즘은 주어진 문자열의 최장 팰린드롬 부수열의 길이를 구하는 알고리즘이다. 
우선, 입력받은 문자열의 길이 n에 대해 2차원 DP 테이블 dp를 생성하고 모든 값들을 0으로 초기화한다.
그리고 문자열의 각 문자가 그 자체로 팰린드롬인 경우 -> dp[i][i]를 1로 초기화한다.
그 다음은 길이 l을 2부터 n까지 순회하면서, 모든 가능한 부분 수열의 팰린드롬 여부를 확인한다. i와 j를 통해 부분 수열의 시작과 끝 인덱스를 나타내며, s[i]와 s[j]가 같은 경우와 다른 경우를 나누어 처리한다.
- s[i]와 s[j]가 같으면, 부분 수열의 양 끝 문자가 같으므로 팰린드롬의 길이를 2 증가시킬 수 있으므로 dp[i][j]를 dp[i+1][j-1] + 2로 업데이트한다.
- s[i]와 s[j]가 다르면, 부분 수열의 양 끝 문자가 다르므로 현재 위치를 하나씩 이동하여 가장 긴 팰린드롬 부분 수열을 찾아야 하므로 dp[i][j]를 dp[i + 1][j]와 dp[i][j-1] 중 큰 값으로 업데이트한다.
dp[0][n-1]을 반환하여 주어진 문자열의 최장 팰린드롬 부분 수열의 길이를 얻습니다.

해당 알고리즘은 2차원 DP 테이블을 사용하며, 문자열의 길이가 n일 때 dp 테이블을 채우는데 이중 반복문을 돌고있다.
외부 반복문은 n-1번 반복으로 O(n), 내부 반복문은 l값에 따라 (n-1)+(n-2)+...+2+1번 반복되며 총 (n-1)n/2번 실행되어 O(n^2)이므로 전체 시간복잡도는 O(n^2)이다.
'''