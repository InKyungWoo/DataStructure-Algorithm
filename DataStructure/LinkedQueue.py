
# 단순연결리스트 큐  # 이중은 피피티에

class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.tail = None
        
    def isEmpty(self):
        return self.front == None
    def clear(self):
        self.front = None
        self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.front.data

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.front = node
            self.tail = node
        else:
            self.tail.link = node
            self.tail = node
    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            if self.front.link == None:
                self.front = None
                self.tail = None
            else:
                self.front = self.front.link
            return data

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.front
            while not node == self.tail:
                node = node.link
                count += 1
            return count
    def display(self, msg = "LinkedQueue: "):
        print(msg, end='')
        if not self.isEmpty():
            node = self.front
            while not node == self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end=' ')
        print()
