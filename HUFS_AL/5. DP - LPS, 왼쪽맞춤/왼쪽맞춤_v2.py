W = int(input())
words = input().split()
# code below

n = len(words)  # 단어들의 개수

# dp 테이블 생성 및 초기화
dp = [float('inf')] * (n + 1)  # dp[i]는 i번째 단어까지 왼쪽 맞춤을 했을 때 발생하는 패널티의 최솟값
dp[0] = 0  # 초기값 설정

# 왼쪽 맞춤 DP 알고리즘 수행
for i in range(1, n + 1):  # 각 단어를 끝으로 하는 줄을 만들 때의 패널티를 계산하기 위해 반복
    width = 0  # 줄의 길이
    for j in range(i, 0, -1):  # 현재 단어부터 역순으로 이전 단어들을 확인
        width += len(words[j - 1]) + 1  # 현재 단어의 길이와 공백의 길이를 더해 줄의 길이 계산
        if width - 1 > W:  # 줄의 길이가 최대 길이를 초과하면 더 이상 확인할 필요 없음
            break
        cost = (W - (width - 1)) ** 3  # 현재 줄을 왼쪽 맞춤할 때 발생하는 패널티 계산
        dp[i] = min(dp[i], dp[j - 1] + cost)  # 현재 패널티와 이전 단어까지의 패널티와의 합 중 최솟값을 선택하여 dp[i]에 저장

print(dp[n])  # 전체 패널티의 최솟값 출력
