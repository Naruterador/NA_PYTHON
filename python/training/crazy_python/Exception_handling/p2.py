#coding=utf-8
'''
多异常捕获
python的一个except块可以捕获多种类型的异常。
在使用一个except块捕获多种异常时，只要将多个异常类用圆括号括起来，中间用逗号隔开即可--其实就是
构建多个异常类的元组。
'''

import sys

try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = a / b
	print("输入的两个数相除的结果是: %d" % c)
except(IndexError,ValueError,ArithmeticError):
	print("程序发生了数组越界、数字格式、算术异常之一")
except Exception:
	print("未知异常")


