
# if문

grade = 80
if grade > 30:
    print('합격입니다.')

# if-else

age = 18 # 입력받는다면 age = int(input())
if age >= 19:
    print('당신은 성인입니다.')
    print(age-19, '살 넘음.')
else:
    print('당신은 미성년자입니다.')
    print(19-age, '살이 부족합.')


# 중첩 if
num = -1
if num > 0:
    print('양수!')
elif num < 0:
    print('음수')
else:
    print('0')


# 반복문

for i in range(0, 7, 2):
    print(i)

for i in range(6, -1, -2):
    print(i)

for i in range(3, 8, 2):
    print(i)

sum = 0
for i in range(1, 11):
    sum += i
print('합계: ', sum)

import time
for i in range(1, 11, -1):
    print(i)
    time.sleep(1)
print('Fire!')

# 중첩반복문

for i in range(3):
    for j in range(3):
        print('*')

for i in range(3):
    for j in range(3):
        print('* ', end='')

for i in range(3):
    for j in range(3):
        print('* ', end='')
    print('')

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=' ')
    print()

for i in range(1, 10):
    print('[ ', i, ' 단 ]')
    for j in range(1, 10):
        print(i, '*', j, '=', i * j)
    print()


for i in range(1, 4):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# while문

i = 0
while i < 3:
    print(i)
    i += 1

# break, continue

sum = 0
for i in range(100):
    sum += i
    if sum > 100:
        break
print('sum=', sum, ', i=', i)

sum = 0
for i in range(100):
    if sum > 100:
        continue
    sum += i
print('sum=', sum, ', i=', i)

# 1에서 100까지의 합
count = 1
hap = 0
while count <= 100:
    hap += count
    count += 1
print(hap)

while True:
    color = input('색상 입력: ')
    if color == 'red':
        break
print('프로그램 종료')
