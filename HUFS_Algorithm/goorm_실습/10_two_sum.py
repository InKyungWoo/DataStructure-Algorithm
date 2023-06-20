def two_sum(X, Y, t):
	# 리스트 X의 원소를 key로 하고, 그 값이 t와 일치하게 만드는 Y의 원소를 찾기 위해 hash table을 생성
	hash_table = {x:1 for x in X}		# 해시 테이블 생성 -> O(n)
	for y in Y:	
		if t - y in hash_table:				# for문을 돌며 검사 -> O(n)
			return True
	return False

A = [int(x) for x in input().split()]  # A 입력
B = [int(x) for x in input().split()]  # B 입력
C = [int(x) for x in input().split()]  # C 입력

# 
# 함수 two_sum을 적절한 형식으로 호출해 그 결과를 이용해 결과 출력
for a in A:
	if two_sum(B, C, -a):		# 원소를 하나씩 two_sum함수에 전달하면서 a+b+c=0을 만족하는 쌍이 있는지 확인 -> O(n)
		print(True)
		break
else:		# for문이 interrupt없이 정상적으로 종료된다면 a+b+c=0을 만족하는 쌍이 없는 것이므로 False를 출력
	print(False)

# 수행시간 분석 및 Big-O 표기
'''
해시 테이블을 생성하여 X의 각 원소를 키로 사용하고, 해당 키에 대응하는 값을 1로 설정한다.
생성된 해시테이블로 리스트 Y의 각 원소 y에 대해 t - y가 있는지 검사한다. 
해당하는 값이 있다면, X에서 선택된 원소와 Y에서 선택된 원소의 합이 t와 일치하는 것이므로 True를 반환하고 그렇지 않다면 False를 반환한다.

1. 해시 테이블 생성은 X의 모든 원소를 순회해야 하므로 -> O(n)
2. Y의 각 원소에 대해 해시 테이블에서 t-y 찾기 -> 최악의 경우 모든 원소에 대해 수행한다면 -> O(n)
3. two_sum(B, C, -a)룰 호출하여 검사하는 것은 O(n)이지만 A의 모든 원소에 대해 수행하므로 -> O(n^2)

따라서 전체 알고리즘의 총 수행시간은 O(n^2)이다.
'''

# 참고) O(n^3)에 동작하는 알고리즘
'''
def three_sum(A, B, C):
    for a in A:  # O(n)
        for b in B:  # O(n)
            for c in C:  # O(n)
                if a + b + c == 0:
                    return True  # 적어도 한 쌍의 (a, b, c)가 존재하여 그 합이 0이 되는 경우
    return False  # 그런 쌍이 없음

A = [int(x) for x in input().split()]  # A 입력
B = [int(x) for x in input().split()]  # B 입력
C = [int(x) for x in input().split()]  # C 입력

print(three_sum(A, B, C))
'''
