'''
题目：输出9*9乘法口诀表。
'''


for i in range(1,10):
	for j in range(1,i + 1):
		result = i * j
		print ('%d * %d = % - 3d'% (i,j,result)) #循环的两个数相乘
	print ('')                                   #两个循环的间隔


