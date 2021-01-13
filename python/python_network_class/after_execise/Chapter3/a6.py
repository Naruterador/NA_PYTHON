#输入三个正整数a、b、n，精确计算a/b的结果到小数后n位。


def division(a,b,n):
	c = a / b
	return round(c,n)

print(division(1,3,2))