
def printStep(arr, val):
    print("Step %2d = "%val, end='')
    print(arr)
    
def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i+1);

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        printStep(A, i)

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range (i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True

        if not bChanged: break;
        printStep(A, n-i);
        
        
while True:
    data = [5, 3, 8, 4, 9]
    opt = input("1.선택정렬 2.삽입정렬 3.버블정렬 4.종료 : ")

    if opt == "4":
        break

    elif opt == "1":
        print("Original : ", data)
        selection_sort(data)
        print("Selection : ", data)
        print()

    elif opt == "2":
        print("Original : ", data)
        insertion_sort(data)
        print("Insert : ", data)
        print()

    elif opt == "3":
        print("Original : ", data)
        bubble_sort(data)
        print("Bubble : ", data)
        print()

    else:
        print("잘못 선택하였습니다!!!")
        print()

print("종료합니다!!")
