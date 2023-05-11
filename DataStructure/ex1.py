from ArrayList import *

s1 = ArrayList()
s1.display('파이썬 리스트로 구현한 리스트 테스트 : ')
s1.insert(0, 10)
s1.insert(0, 20)
s1.insert(1, 30)
s1.insert(s1.size(), 40)
s1.insert(2, 50)
s1.display('파이썬 리스트로 구현한 리스트 삽입*5 :')
s1.sort()
s1.display('파이썬 리스트로 구현한 리스트 정렬 후 : ')
s1.replace(2, 90)
s1.display('파이썬 리스트로 구현한 리스트 교체 후 : ')

s1.delete(2)
s1.delete(s1.size()-1)
s1.delete(0)
s1.display('파이썬 리스트로 구현한 리스트 삭제*3 : ')

lst = [1, 2, 3]
s1.merge1(lst)
s1.display('파이썬 리스트 병합 후 ; ')

s2 = ArrayList()
s2.insert(0,10)
s2.insert(0,20)
s2.insert(1,30)
s2.insert(s2.size(),40)
s2.display()

s2.delete(1); s2.delete(s2.size()-1)
s2.display()
