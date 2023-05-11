from BSTNode import *

class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None
    def clear(self):
        self.root = None
    def size(self):
        return count_node(self.root)
    
    def search(self, key): return search_bst(self.root, key)
    def searchValue(self, key): return search_value_bst(self.root, key)
    def findMax(self): return search_max_bst(self.root)
    def findMin(slef): return search_min_bst(self.root)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)
    def delete(self, key):
        self.root = delete_bst(self.root, key)
    def display(self, msg = 'BSTMap: '):
        print(msg, end='')
        inorder(self.root)
        print()


#test program

if __name__ == '__main__':
    map = BSTMap()
    data = [2, 47, 25, 27, 30, 22, 6, 11, 41, 34, 13, 20, 38, 42, 29, 18]

    print("[삽입 연산]: ",data)
    for key in data:
        map.insert(key)
    map.display("[중위 순회: ")
'''
    if map.search(26) != None:
        print("[탐색 26 ] : 성공")
    else: print("[탐색 26 ] : 실패")
    if map.search(25) != None:
        print("[탐색 25 ] : 성공")
    else: print("[탐색 25 ] : 실패")

    map.delete(3); map.display("[  3 삭제] : ")
    map.delete(68); map.display("[ 68 삭제] : ")
    map.delete(18); map.display("[ 18 삭제] : ")
    map.delete(35); map.display("[ 35 삭제] : ")
'''





    
