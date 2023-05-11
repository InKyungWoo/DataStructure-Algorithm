
from CircularQueue import *

def isValidPos(x,y):
    if x < 0 or y < 0 or x >= MAX_SIZE or y >= MAX_SIZE:
        return False
    else:
        return map[x][y] == '0' or map[x][y] == 'x'

def BFS():
    que = CircularQueue()
    que.enqueue( (1,0) )
    print('BFS: ')

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x, y = here
        if map[x][y] =='x':
            return True
        else:
            map[x][y] = '.'
            if isValidPos(x-1, y): que.enqueue( (x-1,y) ) #상
            if isValidPos(x+1, y): que.enqueue( (x+1,y) ) #하
            if isValidPos(x, y-1): que.enqueue( (x,y-1) ) #좌
            if isValidPos(x, y+1): que.enqueue( (x,y+1) ) #우

    return False

map = [ ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '1', '0', '0', '1'],
        ['1', '0', '0', '0', '1', '1'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '0', 'x'],
        ['1', '1', '1', '1', '1', '1'] ]

MAX_SIZE = 6
result = BFS()

if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')
    
