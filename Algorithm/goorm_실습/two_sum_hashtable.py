def two_sum(X, Y, t):
    # 리스트 X의 원소를 key로 하고, 그 값이 t와 일치하게 만드는 Y의 원소를 찾기 위해 hash table을 생성합니다.
    hash_table = {x:1 for x in X}
    for y in Y:
        if t - y in hash_table:
            return True
    return False

A = [int(x) for x in input().split()]  # A 입력
B = [int(x) for x in input().split()]  # B 입력
C = [int(x) for x in input().split()]  # C 입력

# A의 각 원소 a에 대해, B와 C에서 두 수를 뽑아 그 합이 -a가 되는지 확인합니다.
for a in A:
    if two_sum(B, C, -a):
        print(True)
        break
else:
    print(False)
