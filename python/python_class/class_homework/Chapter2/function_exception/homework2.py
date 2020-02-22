'''
题目：一个五位数，判断他是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

x = int(input("input a number:\n"))
x = str(x)
flag = True
for i in range(len(x) // 2):
	if x[i] != x[-i - 1]:
		flag = False
if flag:
	print("这是一个回文数")
else:
	print("这不是一个回文数")
