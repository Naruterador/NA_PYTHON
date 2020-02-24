#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…，求出这个数列的前20项之和。


#fib_function
def fib_deno(n):
	f1 = 1
	f2 = 1
	f3 = 0
	for i in range(n):
		f3 = f2
		f2 = f1 + f2
		f1 = f3
	return f2

def fib_nume(n):
	f1 = 1
	f2 = 1
	f3 = 0
	for i in range(n):
		f3 = f2
		f2 = f1 + f2
		f1 = f3
	return f1


#fib_recursion
def fib_recursion(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib_recursion(n - 1) + fib_recursion(n - 2)

#recursion
def add_recursion(n):
	sum1 = 0
	denominator = []
	numerator = []

	for i in range(1,n + 1):
		numerator.append(fib_recursion(i))
	for j in range(2,n + 2):
		denominator.append(fib_recursion(j))
	print(denominator,numerator)
	for s2,s1 in zip(denominator,numerator):
		sum1 = sum1 + s2 / s1
	return sum1





#loop
def add_loop(n):
	denominator = 0
	numerator = 0
	sum1 = 0
	for i in range(1,n + 1):
		denominator = fib_deno(i)
		numerator = fib_nume(i)
		sum1 = sum1 + (denominator / numerator)
		print(denominator,numerator)
	return sum1


