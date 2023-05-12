Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> print("Hello World!')
      
SyntaxError: EOL while scanning string literal
>>> print(2+3)
5
>>> 2+3
5
>>> 2*3
6
>>> 2**3
8
>>> 2^3
1
>>> 2/3
0.6666666666666666
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 10%3
1
>>> print(2345*9876-5678)
23153542
>>> print("Hello" + "World!")
HelloWorld!
>>> print("Hello")
Hello
>>> print("Hello" + 3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("Hello" + 3)
TypeError: can only concatenate str (not "int") to str
>>> print("Hello" * 3)
HelloHelloHello
>>> type("hello")
<class 'str'>
>>> type(3)
<class 'int'>
>>> type(3.5)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> print("결과 값은", 2 * 7, "입니다.")
결과 값은 14 입니다.
>>> print(3 + 3.5)
6.5
>>> print("Hello", 3)
Hello 3
>>> print("100" + "200")
100200
>>> print(100 + 200)
300
>>> x = 10
>>> x = 11
>>> y = 10
>>> x + y
21
>>> x = x + y
>>> x
21
>>> x = x + 10
>>> x
31
>>> y = y + 5
>>> y
15
>>> x += 2
>>> x
33
>>> y -=2
>>> y
13
>>> x %= y
>>> x
7
>>> 2 * (3**(1+2))
54
>>> 5 + (6**2 / (1+2)**2)
9.0
>>> float(5 + (6**2 / (1+2)**2))
9.0
>>> 