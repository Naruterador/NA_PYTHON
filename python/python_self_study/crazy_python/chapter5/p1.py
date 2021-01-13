#coding=utf-8

def fn(n):
	if n == 0:
		return 1
	elif n == 1:
		return 4
	else:
		return 2 * fn(n-1) + fn(n-2)


print(fn(4))