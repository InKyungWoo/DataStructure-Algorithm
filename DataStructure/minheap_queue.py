class minheap: #큐버전으로 구현
    def __init__(self):
        self.queue = [None]

    def swap(self, x, y):
        self.queue[x], self.queue[y] = self.queue[y], self.queue[x]

    def insert(self, n):
        self.queue.append(n)
        i = len(self.queue) - 1
        while i>1: #root로 올 때가지 부모와 비교하며 더 작으면 교체
            parent = i // 2
            if self.queue[i] < self.queue[parent]:
                self.swap(i, parent)
                i = parent
            else: break

    def delete(self):
        if len(self.queue) > 1:
            self.swap(1, len(self.queue)-1) #마지막 원소와 root를 바꿔주고
            ans = self.queue.pop(len(self.queue)-1) #마지막 원소 제거 (즉 처음의 root를 제거)
            self.minHeapify(1) #root에서부터 heapiffy를 시작
        else: ans = 0
        return ans

    def leftchild(self, i):
        return i*2
    def rightchild(self, i):
        return i*2 + 1

    def minHeapify(self, i): #자식들과 자신을 비교하면서 내려가는 함수.
        left = self.leftchild(i)
        right = self.rightchild(i)
        smallest = i #일단 작은 걸 자신으로 놓고

        if left <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]:
            smallest = left
        if right <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.minHeapify(smallest)

