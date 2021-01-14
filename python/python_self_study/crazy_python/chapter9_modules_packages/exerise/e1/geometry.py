#coding = utf - 8


__doc__ = '本模块需要先对模块中的类进行初始化才可以使用类名称为Print_shape，带入参数为层数'


'''
定一个geometry模块，在该模块下定义print_triangle(n)和print_diamand(n)两个函数
分别用于在控制台用星号打印三角形和菱形，并为模块和函数都提供文档说明。



abs() 函数返回数字的绝对值。

以下展示了使用 abs() 方法的实例：
print "abs(-45) : ", abs(-45)
print "abs(100.12) : ", abs(100.12)
print "abs(119L) : ", abs(119L)
以上实例运行后输出结果为：
abs(-45) :  45
abs(100.12) :  100.12
abs(119L) :  119
'''
import sys
import os 



class Print_shape(object):
	#函数的说明文档
	__doc__ = 'This function is used to type a triangle.'
	
	#定义__file__变量，文件的路经
	__file__ = os.path.abspath(__file__)

	#使用__all__属性输出可以调用的模块的函数
	__all__ = ['output_triangle','ouput_diamand']

	def __init__(self,layer):
		self.layer = layer


	#用星号打印三角形
	def __print_triangle(self,n):
		if n < 2:
			raise ValueError('Please type the number bigger than 2!')
		for i in range(n):
			print(' ' * ((n - (i + 1))),end='')
			print('*' * ((2 * n - 1) - (2 * (n - (i + 1)))),end='')
			print(' ' * (n - (i + 1)))


	#用星号打印菱形
	def __print_diamand(self,n):
		if n < 2:
			raise ValueError('Please type the number bigger than 2!')
		for i in range(2 * n - 1):
			if i > n - 1:
				print(' ' * abs(((n - (i + 1)))),end='')
				print('*' * ((2 * n - 1) - (2 * abs((n - (i + 1))))),end='')
				print(' ' * abs((n - (i + 1))))
				
			else:
				print(' ' * ((n - (i + 1))),end='')
				print('*' * ((2 * n - 1) - (2 * (n - (i + 1)))),end='')
				print(' ' * (n - (i + 1)))




	def output_triangle(self):
		self.__print_triangle(self.layer)

	def ouput_diamand(self):
		self.__print_diamand(self.layer)




