'''
一个正整数分解质因数，例如:输入90，输出2*3*3*5
'''



n = input("Enter an integer:")
n = int(n)
first = True
print(n,end="")

i = 2
while i <= n:
	while n % i == 0:
		if first:
			print("=",end="")
			print(i,end="")
			first = False
		else:
			print("*",end="")
			print(i,end="")
		n = n // i
	i = i + 1