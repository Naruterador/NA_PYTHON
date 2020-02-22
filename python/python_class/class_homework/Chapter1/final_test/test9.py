'''
题目：求s = a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如 2+22+222+222...2（此时共有5个数相加），几个数相加有键盘控制。
'''


from functools import reduce

Tn = 0
Sn = []
n = int(input('n = :'))
a = int(input('a = :'))

for count in range(n):
	Tn = Tn + a
	a = a * 10
	Sn.append(Tn)


result = reduce(lambda x,y : x + y,Sn)
print(result)

