
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search_bst(n,key):
    if n == None: return None
    elif key == n.key: return n
    elif key < n.key: return search_bst(n.left, key)
    else: return search_bst(n.right, key)
        
def search_bst_iter(n, key):
    while n != None:
        if key == n.key: return n
        elif key < n.key: n = n.left
        else: n = n.right
    return None
    
def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n
def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end= ' ')
        inorder(n.right)

def levelorder(n):
    que = []
    que.append(n)
    while len(que) != 0:
        n = que.pop(0)
        if n is not None:
            print(n.key, end = ' ')
            que.append(n.left)
            que.append(n.right)   

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
    
def insert_bst(r,n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False
        
def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root
def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root: root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root
def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right
    while succ.left != None:
        succp = succ
        succ = succ.left

    if succp.left == succ :
        succp.left = succ.right
    else:
        succp.right = succ.right
    node.key = succ.key
    node.value = succ.value
    node = succ;

    return root
        
def delete_bst(root,key):
    if root == None: return None

    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key: node = node.left
        else: node = node.right;

    if node == None: return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)
    return root






            
