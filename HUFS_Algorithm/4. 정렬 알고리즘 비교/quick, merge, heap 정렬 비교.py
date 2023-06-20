import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##

# 1. Quick sort
def quick_sort(A, first, last):
	
	global Qc, Qs		# 비교 횟수 Qs, swap 횟수 Qs
	
	if first >= last : return
	left, right = first + 1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			Qc += 1		# 비교
		while right > first and A[right] > pivot:
			right -= 1
			Qc += 1		# 비교
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -=1
			Qs += 1		# swap
	
	A[first], A[right] = A[right], A[first]
	Qs += 1		# swap
	quick_sort(A, first, right-1)
	quick_sort(A, right+1, last)


# 2. Merge sort
def merge_sort(A, first, last):
	
	global Mc, Ms
	
	if first >= last: return
	merge_sort(A, first, (first+last)//2)
	merge_sort(A, (first+last)//2 +1, last)
	merge_two_sorted_lists(A, first, last)
	
def merge_two_sorted_lists(A, first, last):
	
	global Mc, Ms
	
	m = (first + last) // 2
	i, j = first, m+1
	B = []
	while i <= m and j <= last:
		Mc += 1		# 비교
		if A[i] <= A[j]:
			B.append(A[i])
			i += 1
		else:
			B.append(A[j])
			j += 1
	for k in range(i, m+1):
		B.append(A[k])
		Ms += 1		
	for k in range(j, last+1):
		B.append(A[k])
		Ms += 1
	for k in range(first, last+1):
		A[k] = B[k-first]
		Ms += 1


# 3. Heap sort
def heapify_down(A, k, n):
	
	global Hc, Hs
	
	if n == 0: return None
	
	while 2*k +1 < n:
		L, R = 2*k +1, 2*k + 2
		if L < n and A[L] > A [k]:
			m = L
			Hc += 1		# 비교
		else:
			m = k
			Hc += 1		# 비교
		if R < n and A[R] > A[m]:
			m = R
			Hc += 1		# 비교
		if m != k:
			A[k], A[m] = A[m], A[k]
			k = m
			Hs += 1		# swap
		else:
			break
	
def make_heap(A):
	n = len(A)
	for k in range(n//2 -1, -1, -1):
		heapify_down(A, k, n)

def heap_sort(A):
	
	global Hc, Hs
	
	n = len(A)
	make_heap(A)
	
	for k in range(n-1, -1, -1):
		A[0], A[k] = A[k], A[0]
		Hs += 1		# swap
		n -= 1
		heapify_down(A, 0, n)


# [추가점수1: quick sort] - k(10~40)개 이하가 되면 분할을 멈추고 insertion sort

def insertion_sort(A, first, last):
	
	global Qc_2, Qs_2
	
	for i in range(first+1, last+1):
		j = i-1
		Qc_2 += 1	
		while j >= 0 and A[j] > A[j+1]:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1
			Qc_2 += 1	
			Qs_2 += 1


def quicksort_with_insertion(A, first, last):
	
	global Qc_2, Qs_2
	
	if (last - first+1) >= 10 and (last - first+1) <= 40:		# 이 때 분할 멈추고 insertion_sort 실행
		insertion_sort(A, first, last)
		return
	
	# 나머지는 quick_sort와 동일
	if first >= last : return
	left, right = first + 1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			Qc_2 += 1		# 비교
		while right > first and A[right] > pivot:
			right -= 1
			Qc_2 += 1		# 비교
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -=1
			Qs_2 += 1		# swap
	
	A[first], A[right] = A[right], A[first]
	Qs_2 += 1		# swap
	quicksort_with_insertion(A, first, right-1)
	quicksort_with_insertion(A, right+1, last)
	
	
# [추가 점수 3: merge sort] 3-way merge sort

def merge_sort_3way(A, first, last):
	
	global Mc_2, Ms_2
	
	if first >= last:
		return A
	else: 
		mid1 = first + ((last - first) // 3)
		mid2 = first + 2 * ((last-first) // 3)

		merge_sort_3way(A, first, mid1)
		merge_sort_3way(A, mid1+1, mid2 + 1)
		merge_sort_3way(A, mid2+2, last)
		Mc_2 += 2
		Ms_2 += 1
		merge_3way(A, first, mid1, mid2, last)
		return A

def merge_3way(A, first, mid1, mid2, last):
	
	global Mc_2, Ms_2

	L = A[first -1 : mid1]
	M = A[mid1: mid2 + 1]
	R = A[mid2 + 1 : last]

	L.append(float('inf'))
	M.append(float('inf'))
	R.append(float('inf'))
    
	left = 0
	mid = 0
	right = 0
	for i in range(first-1, last):
		minimum = min([L[left], M[mid], R[right]])
		Mc_2 += 2
		if minimum == L[left]:
			A[i] = L[left]
			left += 1
			Ms_2 += 1
		elif minimum == M[mid]:
			A[i] = M[mid]
			mid += 1
			Ms_2 += 1
		else:
			A[i] = R[right]
			right += 1
			Ms_2 += 1


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
Qc_2, Qs_2, Mc_2, Ms_2 = 0, 0, 0, 0

n = int(input())
random.seed()
A = []		# quick sort
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]	# merge sort
C = A[:]	# heap sort
D = A[:]	# quick + insertion sort
E = A[:]	# 3-way merge sort
F = A[:]	# tim sort

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("Quick sort with Insertion:")
print("time =", timeit.timeit("quicksort_with_insertion(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc_2, Qs_2))

print("3-way Merge sort:")
print("time =", timeit.timeit("merge_sort_3way(E, 1, n)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc_2, Ms_2))

print("Tim sort:")
print("time =", timeit.timeit("sorted(F)", globals=globals(), number=1))
# Tim sort는 파이썬 내장 함수로 수행시간 바로 측정


# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))		# quick_sort 확인
assert(check_sorted(B))		# merge_sort 확인
assert(check_sorted(C))		# heap_sort 확인
assert(check_sorted(D))		# quicksort_with_insertion 확인
assert(check_sorted(E))	# 3-way merge 확인
assert(check_sorted(sorted(F)))		# tim sort 확인
