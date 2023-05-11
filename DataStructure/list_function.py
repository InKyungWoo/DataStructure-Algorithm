
items = []

def insert(pos, elem):
    items.insert(pos, elem)
def delete(pos):
    return items.pop(pos)
def clear():
    items = []
def display():
    print(items)

insert(0, 10); insert(0, 20); insert(1, 30); insert(len(items), 40)
display()
delete(1); delete(len(items)-1)
display()
clear()
display()
