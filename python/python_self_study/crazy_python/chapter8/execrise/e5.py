#coding = utf - 8

'''
自定义一个生成器，可依次返回1,2,3,4....的阶乘。
'''

#定义一个阶乘的生成器

def Factorial(val):

	result = 1
	for i in range(1,val+1):
		result = result * i
		yield result



p = Factorial(4)

print(next(p))
print(next(p))
print(next(p))
print(next(p))
