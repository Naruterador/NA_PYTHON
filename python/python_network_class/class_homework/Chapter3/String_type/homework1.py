#输入一个字符串s,反向输出它，例如输入"abc"，输出"cba"

s = input("Please input the your string:")
i = len(s) - 1 
while i >=0:
	print(s[i],end="")
	i -= 1

print()

