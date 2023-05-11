
from CircularQueue import *

class TNode:
    def __init__(self,data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end= ' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end = ' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1

if __name__ == '__main__':
    d = TNode('D', None, None)
    e = TNode('E', None, None)
    g = TNode('G', None, None)
    b = TNode('B', None, d)
    f = TNode('F', g, None)
    c = TNode('C', e, f)
    
    root = TNode('A', b, c)

    print('\n In-Order : ', end='')
    inorder(root)
    print('\n Pre-Order : ', end='')
    preorder(root)
    print('\n Post-Order : ', end='')
    postorder(root)
    print('\n Level-Order : ', end='')
    levelorder(root)
    print()

    print("노드의 개수 = %d개" % count_node(root))
    print("단말의 개수 = %d개" % count_leaf(root))
    print("트리의 높이 = %d" % calc_height(root))
    
