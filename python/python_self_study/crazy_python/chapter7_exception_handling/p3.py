#coding=utf-8
'''
访问异常信息：

如果程序需要在except块中访问异常对象的相关信息，则可通过为异常对象声明变量来实现。
当python解释器决定调用某个except块来处理该异常对象时，会将异常对象赋值给except块后的异常变量
程序可以通过该变量来获得异常的对象的相关信息。
'''

'''
所有的异常对象都包含了如下几个常用属性和方法:

1.args:该属性返回异常的错误编号和描述字符串
2.errno:该属性返回异常的错误编号
3.strerror:该属性返回异常的描述字符串
4.with_traceback():通过该方法可处理异常的传播轨迹信息
'''

def foo():
	try:
		fis = open("a.txt")
	except Exception as e:
		print(e.args)
		print(e.errno)
		print(e.strerror)
		print(e.with_traceback)

foo()
