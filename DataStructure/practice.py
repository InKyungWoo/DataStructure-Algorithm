import random

def prefixSum1(X, n):
    for i in range(0, n):
        S = []
        sum = 0
        for j in range(0, i+1):
            sum += X[j]
            S.append(sum)
    print(S)


def prefixSum2(X, n):
    S = []
    sum = 0
    S.append(X[0])
    for i in range(1, n):
        sum = S[i-1] + X[i]
        S.append(sum)
    print(S)
        
n = int(input())
X = []
for i in range(n):
    num = random.randint(1, 50)
    if num not in X:
        X.append(num)
print(X)
prefixSum1(X, n)
prefixSum2(X, n)

