#计算1+2+4+……+100的和。

#recursion
def add_recursion(n):
	if n == 1:
		return 1
	else:
		return ((2 * n) + add(n - 1)) - 2 


#loop
def add_loop(n):
	sum = 1
	for i in range(0,n):
		sum = sum + 2 * i
	return sum

