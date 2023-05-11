class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return str("%s:%s"%(self.key, self.value))


def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i].key == key:
            return i
    return None

def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle].key:
            return middle
        elif key < A[middle].key:
            return binary_search(A, key, low, middle - 1)
        else:
            return binary_search(A, key, middle+1, high)
    return None


if __name__ == '__main__':
    while True:
        
        arr = [ Entry(2,'a'), Entry(6,'b'), Entry(11,'c'), Entry(13,'d'),
                Entry(18,'e'),Entry(20,'f'), Entry(22,'g'), Entry(27,'h'),
                Entry(29,'i'), Entry(30,'j'), Entry(34,'k'), Entry(38,'l'),
                Entry(41,'m'), Entry(42,'n'), Entry(45,'o'), Entry(47,'p') ]
        opt = input("1.순차탐색 2.이진탐색 3.종료 : ")

        if opt == "3":
            break
        elif opt == "1":
            res = sequential_search(arr, 20, 0, 15)
            for en in arr:
                print(en, end=" ")
            print('\nkey=20 : value={}'.format(arr[res].value))
        elif opt == "2":
            res = binary_search(arr, 27, 0, 15)
            for en in arr:
                print(en, end=' ')
            print('\nkey=27 : value={}'.format(arr[res].value))
        else:
            print("잘못 선택하였습니다!!!")
    print("종료합니다!!!")
              



