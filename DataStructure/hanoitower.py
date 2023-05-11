

def hanoi_tower(n, fr, tmp, to):
    global count

    if n == 1:
        print("원판 1: %s --> %s" % (fr, to))
        count += 1
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)
        count += 1


for i in range(1, 5):
    count = 0
    hanoi_tower(i, 'A', 'B', 'C')
    print("총횟수 : %s" % count, end="\n====================\n")
    i += 1
    
