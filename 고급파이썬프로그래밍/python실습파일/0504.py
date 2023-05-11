# 6. 객체지향
'''
class You:
	def __init__(self, n, a): # 맴버변수를 초기화하는 메소드
		self.name = n
		self.age = a
	def show(self): 
		print('이름:', self.name, '나이:',self.age)
my = You('준서',21)
my2 = You('준희',20)
my.show()
my2.show()


# 이름과 나이 입력받기 - 
class You:
	def __init__(self): # 맴버변수를 초기화하는 메소드
		self.name = input('이름: ')
		self.age = int(input('나이: '))
	def show(self): 
		print('이름:', self.name, ', 나이:',self.age)
my = You()
my2 = You()
my.show()
my2.show()


# 이름과 나이 입력받기 - 반복문 사용
class You:
	def __init__(self): # 맴버변수를 초기화하는 메소드
		self.name = input('이름: ')
		self.age = int(input('나이: '))
	def show(self): 
		print('이름:', self.name, ', 나이:',self.age)
student = []
for i in range(2):
    student.append(You())
for i in range(len(student)):
    student[i].show()


class Calc:
    def __init__(self, n):
        self.a = n
    def plus(self, value):
        print(self.a, '=', value, '=', self.a + value)
    def mult(self, value):
        print(self.a, '*', value, '=', self.a * value)
my = Calc(3)
my.plus(7)
my.mult(10)
         
# quiz 6.2
class Calc:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2
    def calculate(self, op):
        if(op == '+'):
            print(self.a, '+', self.b, '=', self.a + self.b)
        elif (op == '*'):
            print(self.a, '*', self.b, '=', self.a * self.b)
num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
obj = Calc(num1, num2)
obj.calculate('+')
obj.calculate('*')


# 데이터형 객체
def func(x):
    x = 5
    print('x(함수):', x)
x = 3
func(3)
print('x(메인):', x)

# swap
def swap(aa, bb):
    print('2: id(aa)', id(aa), 'id(bb)', id(bb))
    return bb, aa
a = 3
b = 5
print('a=', a, 'b=', b)
print('1: id(a)', id(a), 'id(b)', id(b))
a, b = swap(a, b)
print('3 : id(a)', id(a), 'id(b)', id(b))
print('a=', a, 'b=', b)


# quiz 6.4 - 피보나치
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end='')
        a, b = b, a+b
fib(8)

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
a = fib2(8)
print(a)

# for문 반복
a = [2, 6, 9, 0, 9, 1, 7]
for x in a:
    print(x, end='')

a = [[9,9], [0,4], [2,3]]
for x, y in a:
    print(x, y)

b = [[9,9,9], [0,4,4]]
for x, y, z in b:
    print(x, y, z)

# frequency
text = "AI! 나는 인공지능 로봇 입니다. 나는 'AI 로봇' 입니다."
def max_counts(text):
    counts ={}
    for i in text.split(' '):
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
max_counts(text)            # 함수 호출
print(max_counts(text))     # 함수 출력

# quiz 6.6 - 특수기호 제외
text = "AI! 나는 인공지능 로봇 입니다. 나는 'AI 로봇' 입니다."
def max_counts(text):
    skips = ['.', ',', ';', ':', "'", '!'] # 외따옴표는 쌍따옴표로 묶기
    for ch in skips:
        text = text.replace(ch, '')
    counts ={}
    for i in text.split(' '):
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
max_counts(text)            # 함수 호출
print(max_counts(text)) 


# 성씨 빈도수 구하기
people = ['홍', '이', '김', '이', '이', '김']
def max_count(people):
    counts = {}
    for i in people:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
counts = max_count(people)
print(counts)
print(max(counts))                      # 가장 큰 키(key): '홍' > '김' (가나다순)
print(max(counts, key = counts.get))    # 가장 큰 값(value): 3 > 2
print(max(counts.values()))
for name, count in counts.items():
    print(name, count)

print(min(counts))
print(min(counts, key = counts.get))
'''

# quiz 6.10
people = ['홍', '이', '김', '이', '이', '김']
def max_count(people):
    counts = {}
    for i in people:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
counts = max_count(people)
first = []
max_num = max(counts.values())
for name, count in counts.items():
    print(name, ':', count, '번')
    if count == max_num:
        first.append(name)
print('1등:', first)






    




