Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #3/16 고파썬프로그래밍
>>> a = 3
>>> b, c = 2, 1
>>> x,y,z = 10,20,30
>>> a>b
True
>>> b<c
False
>>> a=b
>>> a
2
>>> a==b
True
>>> b!=c
True
>>> x <= z
True
>>> x >= y
False
>>> a>x and b>c
False
>>> a>x and b<c
False
>>> a>x or b>c
True
>>> not(a>x and b>c)
True
>>> not(a>x or b>c)
False
>>> aa = 0o11
>>> aa
9
>>> bb = 0o03
>>> bb
3
>>> cc = 0x11
>>> cc
17
>>> a = 3
>>> print("%d" %a)
3
>>> print("%f" %a)
3.000000
>>> print("%s" %a)
3
>>> name = input('이름: ')
이름: 우인경
>>> print(name)
우인경
>>> num = input('좋아하는 숫자는: ')
좋아하는 숫자는: 3
>>> print(num)
3
>>> type(num)
<class 'str'>
>>> num
'3'
>>> num2 = int(input('좋아하는 숫자는: '))
좋아하는 숫자는: 33
>>> num2
33
>>> type(num2)
<class 'int'>
>>> b = '5.5'
>>> bype(b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    bype(b)
NameError: name 'bype' is not defined
>>> type(b)
<class 'str'>
>>> print(int(b))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(int(b))
ValueError: invalid literal for int() with base 10: '5.5'
>>> bb = '5'
>>> type(bb)
<class 'str'>
>>> print(float(bb))
5.0
>>> a = input('참(True)/거짓(False): ')
참(True)/거짓(False): False
>>> print(bool(a))
True
>>> a = input('참(1)/거짓(0): ')
참(1)/거짓(0): 0
>>> print(bool(a))
True
>>> aa = int(a)
>>> print(bool(aa))
False
>>> print(bool(7))
True
>>> print(bool(00))
False
>>> print(bool(3))
True
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
나이: 21
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
나이: 21
Traceback (most recent call last):
  File "/Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py", line 3, in <module>
    if age >= 19:
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
나이: 21
성인입니다.
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
나이: 18
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
나이: 100
성인입니다.
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
나이: 10
성인이 아닙니다.
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
나이: 31
성인입니다.
12 살 넘음.
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
나이: 18
성인이 아닙니다.
1 살이 부족함.
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
음수
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
number: 3
양수!
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
number: -3
음수
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
number: 0
0
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
number: -20
음수
>>> 
= RESTART: /Users/inkyung/Desktop/고급파이썬프로그래밍/찐파이썬.py
number: 20
양수!
>>> 