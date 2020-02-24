#有一个数序列：1,2,3，5，8，13，21...，用while循环求出这个数列的前20项之和。

def fib_change(n):
	f1 = 1
	f2 = 1
	f3 = 0
	sum1 = 0
	while n > 0:
		f3 = f2
		f2 = f1 + f2
		f1 = f3
		sum1 = sum1 + f1
		n -= 1
		
	return sum1

