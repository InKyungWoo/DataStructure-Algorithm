'''
# 각 자리 숫자의 합

n = 1234
sum = 0
while n >0:
    number = n % 10
    sum += number
    n = n // 10
print(sum)


# 7의 배수 출력, for문, if문 사용
for i in range(1, 31):
    if i % 7 == 0:
        print('7의 배수: ', i)
print('\n')

# 7의 배수 출력, for문, if~continue문 사용 
for i in range(1, 31):
    if i % 7 != 0:
        continue
    print('7의 배수: ', i)
    
        
# 예외처리 구문

try:
    num = 6/2
except:
    print("0으로 나눌 수 없습니다!")
    print("오류나면 실행!")
else:
    print("오류 없으면 실행!", num)
finally:
    print("매번 실행: good!")
    

# 단수반환, 지역변수, 전역변수

def double(n):
    global square # 전역변수 선언
    square= n * n
    return square

print(double(7))
print(square) # name errer -> local variable


# 복수반환
def add_sub(a, b):
    sum = a + b
    diff = a - b
    mul = a * b
    rem = a % b
    return sum, diff, mul, rem
print(add_sub(15, 6))


# 두 수의 교환
def swap(a, b):
    return b, a

a, b = 3, 5
a, b = swap(a, b)
print('a=', a, 'b=', b)


# 52a. Quiz 4.1 -(2)

def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result
print('9! =', factorial(9))


# math모듈
import math
print('9! =', math.factorial(9))


# random 모듈
import random
print(random.randint(1,3))
print(random.randint(50,100))
    

#함수의 응용

#지역변수 전역변수
def calculate_area(radius):
    global area
    area = 3.14 * radius **2
    return
area = 0
r = 5.0
calculate_area(r)
print(area)


# 1~10까지 짝수의 합과 홀수의 합을 구하는 함수
def evenOdd():
    even_sum = 0
    odd_sum = 0
    for i in range(1, 11):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    print("짝수의 합: ", even_sum)
    print("홀수의 합: ", odd_sum)
evenOdd()
'''

n, m = 12345, 987654
print('{0:3,.2f} {1:5,.1f}'.format(n,m))
