W = int(input())
words = input().split()
# code below

n = len(words)  # 단어들의 개수

# dp 테이블 생성, 공백으로 초기화
dp = [None] * (n + 1)  # i번째 단어까지 왼쪽 맞춤을 했을 때 발생하는 penalty의 최솟값
dp[0] = 0  # 초기값 설정

for i in range(1, n + 1):
	width = 0
	for j in range(i, 0, -1):  # 현재 단어부터 역순으로 이전 단어들을 확인
			width += len(words[j-1]) + 1  # 현재 단어의 길이와 공백의 길이를 더해 줄의 길이 계산
			if width - 1 > W:  # 줄의 길이가 최대 길이를 초과하면 -> 더 이상 확인할 필요 X
				break
			cost = (W - (width-1)) ** 3  # 현재 줄을 왼쪽 맞춤할 때 발생하는 penalty 계산

			#dp[i]=None인 경우, dp[j-1] + cost로 업데이트
			#그게 아니면,dp[i]와 dp[j-1]+cost 중 작은 값으로 업데이트
			dp[i] = min(dp[i], dp[j-1] + cost) if dp[i] is not None else dp[j-1] + cost  

print(dp[n])  # 최소 penalty 값


'''
[점화식]
1) if dp[i] == None, dp[i] = dp[j-1] + cost
2) if dp[i] != None, dp[i] = min(dp[i], dp[j-1] + cost)

위 점화식은 dp[i]를 계산하는 점화식으로 i번째 단어까지 왼쪽 맞춤을 했을 때 발생하는 패널티의 최솟값을 구하는 알고리즘이다.
i번째 단어를 끝으로 하는 줄을 만들 때의 패널티를 계산하기 위해 반복적으로 이전 단어들을 확인하고, 이를 위해 j는 i부터 1까지 역순으로 반복하는 이중 반복문의 구조이다.
외부 반복문은 1부터 n까지 반복하므로 O(n)이고, 내부 반복문은 최악의 경우 i번째까지의 모든 이전 단어를 확인하므로 총 i번 반복한다.
최악의 경우 i의 총합은 1부터 n까지의 합인 n(n+1)/2 이므로, 전체 수행시간은 O(n^2)이다.
'''