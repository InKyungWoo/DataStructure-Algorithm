'''
#조건문
age = int(input('나이: '))

if age >= 19:
    print('성인입니다.')
    print(age-19, '살 넘음.')
else:
    print('성인이 아닙니다.')
    print(19-age, '살이 부족함.')
'''

#38p.
#num = -1
num = int(input('number: ')) #숫자 입력받기
if (num > 0):
    print('양수!')
elif (num < 0):
    print('음수')
else:
    print('0')
