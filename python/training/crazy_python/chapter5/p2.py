#coding=utf-8
'''
字典传入函数的参数是指针地址，所以在全局会修改字典的值
'''
#def swap(a,b):
#	a,b = b,a


def swapdw(dw):
	dw['a'],dw['b'] = dw['b'],dw['a']
	#dw = None

dw = {'a':6,'b':9}

print(dw)
swapdw(dw)
print(dw)

#a = 5
#b = 6

#print(a,b)

#swap(5,6)

#print(a,b)