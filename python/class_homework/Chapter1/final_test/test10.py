'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

如果一个正整数 a 是某一个整数 b 的平方，那么这个正整数 a 叫做完全平方数。零也可称为完全平方数。
'''


import math
for i in range(10000):
	x = int(math.sqrt(i + 100))
	y = int(math.sqrt(i + 168))
	if (x * x == i + 100) and (y * y  == i + 168):
		print(i)

