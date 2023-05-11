from minheap import *

def make_tree(freq):
    heap = MinHeap()
    for n in freq:
        heap.insert(n)

    for i in range(0,n):
        e1 = heap.delete()
        e2 = heap.delete()
        heap.insert(e1 + e2)
        print(" (%d + %d)" %(e1, e2))

label = ['E', 'T', 'N', 'I', 'S' ]
freq = [15, 12, 8, 6, 4]
make_tree(freq)
