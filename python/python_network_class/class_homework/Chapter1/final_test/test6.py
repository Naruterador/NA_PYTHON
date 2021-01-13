'''
题目：将一个正整数分解质因数。例如：输入90，打印出90 = 2 * 3 * 3 * 5.
'''

n = int(input("input number:"))
print ("n = %d" % n)

for i in range(2,n + 1):
	while n > i:
		if n % i == 0:
			print(str(i))
			print("*")
			n = n / i
		else:
			break
print( "%d" % n)

