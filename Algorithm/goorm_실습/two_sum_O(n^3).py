def three_sum(A, B, C):
    for a in A:  # O(n)
        for b in B:  # O(n)
            for c in C:  # O(n)
                if a + b + c == 0:
                    return True  # 적어도 한 쌍의 (a, b, c)가 존재하여 그 합이 0
    return False  # 그런 쌍이 없음

A = [int(x) for x in input().split()]  # A 입력
B = [int(x) for x in input().split()]  # B 입력
C = [int(x) for x in input().split()]  # C 입력

print(three_sum(A, B, C))
