def fibo(n):
	if n == 0: return 1
	if n == 1: return 1

	a, b = 1, 1
	i = 2
	while i <= n:
		fib = a + b
		a = b
		b = fib
		i += 1
	return fib

# n을 입력받은 
n = int(input())

# fibo(n) 호출!
result = fibo(n)

# 리턴값을 출력함
print(result)