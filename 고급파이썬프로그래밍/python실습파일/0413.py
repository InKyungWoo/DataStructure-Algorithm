'''
# 2차원 리스트
record = [
    [1, 2, 3],
    [10, 20, 30],
    [100, 200, 300]]
index = [ary[1] for ary in record]
print(index)
print(record[1])
print(record[0])


mylist = [[1,2], [3,4,5], [6,7]]
newlist = [x for x in mylist if len(x)==2]
print(newlist)


# 튜플-중첩
animals = ('토끼','사자','원숭이')
fruits = '사과', '오렌지', 1020, 88
things = animals, fruits
print(things)

# 튜플 내부의 원소로 존재하는 리스트는 수정 가능
fruits = (['포도','망고'],['사과','키위'])
fruits[1][0] = '수박'
print(fruits)

# 튜플을 원소로 갖는 리스트
fruits = [('포도','망고'),('사과','키위')]
fruits[0] = ('수박','참외')
print(fruits)

# 튜플 슬라이싱
dice = (3,2,5,3,4)
print(dice[2:4])

dice1 = (3,2,5,3,4)
dice2 = (6,1,4,2,3)
dice3 = dice1 + dice2
print(dice3)

# 튜플 병합
x = 12.23
y = 23.34
packing = (x,y) #packing!
print('packing:', packing)
c1, c2 = packing #unpacking!
print('c1:', c1)
print('c2:', c2)

# 튜플 반복
a = (1,2,3)
b = a
print(b)

for i in a:
    print(i*2)
print(a)

# quiz 5.15
import random
bigdata = []
nodata = []

for i in range(100):
    bigdata.append(random.randint(1,33))
print(bigdata)

for i in range(1,34):
    if i not in bigdata:
        nodata.append(i)
print('존재하지 않는 값(들):', nodata)

# 딕셔너리
fruitdb = {'사과':1020, '오렌지':880, '포도':3160}
del fruitdb['사과']
print(fruitdb)
fruitdb['바나나']=3200
print(fruitdb)

# 다른 배열로 사전 만들기
student = dict([['현준', 1234], ['민지', 2345]]) #리스트로 이루어진 리스
print(student)
student = dict([('현준', 1234), ('민지', 2345)]) #튜플로 이루어진 리스트
print(student)
student = dict((('현준', 1234), ('민지', 2345))) #튜플로 이루어진 튜플
print(student)

# 집합의 원수 추가 및 삭제
fruits = {'사과','오렌지','포도'}
fruits.update({'수박'})
print(fruits)
fruits.remove('오렌지')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)

# 집합의 연산
one = {1, 3, 5, 7, 8}
two = {1, 3, 5, 6, 8}
print('one | two:', one | two)
print('one & two:', one & two)
print('one - two:', one - two)
print('one ^ two:', one ^ two)

# 빅데이터 분석예제 quiz 5.23
training_data = [['연두', 3, '사과'],
                 ['노랑', 3, '사과'],
                 ['빨강', 2, '포도'],
                 ['빨강', 1, '포도'],
                 ['노랑', 3, '레몬']]
def fruit_counts(data):
    counts = {}
    for row in data:
        color = row[0]
        if color not in counts:
            counts[color] = 0
        counts[color] += 1
    return counts
result = fruit_counts(training_data)
print(result)

# quiz 5.22
word = 'Python Programming'함 # 18개
letters = set(word)
print(len(letters)) # 집합은 중복 제거
print(len(word))    # 공백, 중복문자 포

# quiz 5.21
males = {0, 2, 4, 8, 9}
females = {1, 3, 5, 6, 7}
everyone = males | females
print(everyone & set([1,2,3,10]))
'''
# quiz 5.20
age = {'동혁':21, '민지':19, '준혁':23}
print(age['동혁'])
age['민지'] = age['민지'] + 1
print(age['민지'])

student = {'GilDong':2345, 'SunSin':1234, 'Sejong':3456}
for name in student:
    print(name, ':', student.get(name))

for name, num in student.items():
    print(name, ':', num)


