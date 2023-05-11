# 0406 문자열

ai = 'pyThon proGram'
print('선택수정:', ai.replace('p', 'P'))
print('소문자:', ai.lower())
print('대문자:', ai.upper())
print('swap대소문자:', ai.swapcase())
print('첫문자만 대문자:', ai.capitalize())
print(ai.strip())

text='  python '
print(text.strip())
print(text.rstrip())
print(text.lstrip())
print(text[2])
print(text[::-2])


seq = 'Hello'
for s in seq:
    print(s)

import random
print(random.random())
print(random.randrange(1,2))
print(random.randrange(1.0,2.0))
print(random.randint(1,2))
print(random.choice([1,2,3]))

# 5.5 무작위 문자 병합
import random
pw = str() # 빈 문자열 생성
char = 'python'
for _ in range(10):
    pw += random.choice(char)
print(pw)

# 오렌지만 출력
price = ['사과', '오렌지', '포도', '오렌지', '복숭아', '오렌지']
print(price[::-2])
print(price[::2])
print(price[1::2])

# append()
a = []
for i in range(5):
    a.append(i)
    print(a[i])
print(a)


def new(n, x):
    n = 2
    x.append(x[-1]+1)
    print('new :', n, x)
def one():
    n = 1
    x = [0, 1, 2]
    print('one: ', n, x)
    new(n, x)
    print('one: ', n, x)
one()


#enumerate

animals = ['새','코끼리','강아지']
for i, animal in enumerate(animals):
           print(i, animal)


bird_pos = []
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']
for i, animal in enumerate(animals):
    if (animal =='새'):
        bird_pos.append(i)
print(bird_pos)


# 리스트 comprehension
mylist = [3,5,4,9,1,8,2,1]
newlist = [i for i in mylist if i%2 == 0]
print(newlist)

