class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, pos, elem):
        self.items.insert(pos, elem)
    def delete(self, pos):
        self.items.pop(pos)
    def isEMpty(self):
        return self.size() == 0
    def getEntry(self, pos):
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def find(self, elem):
        return self.items.index(elem)
    def replace(self, pos, elem):
        self.items[pos] = elem
    def sort(self):
        self.items.sort()

    def merge1(self, lst):
        self.items.extend(lst)
    def merge2(self, otherList):
        self.items.extend(otherList.items)

    def display(self, msg = 'Arraylist : '):
        print(msg, '항목수=', self.size(), self.items)
