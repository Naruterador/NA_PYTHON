'''
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又吃了一个，第二天早上又将剩下的桃子吃掉一半
又多吃了一个。以后每天早上都吃了前天剩下的一半零一个。到第十天早上再想吃时，见剩下一个桃子了。求一天共摘了多少。
'''
'''
x2 = 1
for day in range(9,0,-1):
	x1 = (x2 + 1) * 2
	x2 = x1
	print(x1)
print(x1)
'''



def peach(n):
	sum1 = 0

	if n == 10:
		return 1
	else:
		sum1 = peach(n + 1)
		sum1 = (sum1 + 1) * 2

	if n == 1:
		print(sum1)

	return sum1

peach(1)