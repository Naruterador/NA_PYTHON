#计算1+1/3+1/5+……+1/99的和。

#recursion
def division_recursion(n):
	if 1 == n:
		return 1
	else:
		return 1 / (2 * n - 1) + division_recursion(n - 1)


#loop
def division_loop(n):
	sum1 = 0
	denominator = 0

	for i in range(1,n + 1):
		denominator = 2 * i - 1
		sum1 = sum1 + (1 / denominator)
	return sum1

