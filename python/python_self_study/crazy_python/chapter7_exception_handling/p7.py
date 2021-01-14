#coding=utf-8

'''
通常情况下，请不在finally中使用return或者raise等方法导致方法中止的语句，一旦在finally块中使用了return语句
或raise语句，将会导致try块、except块中的return、raise语句失效。
'''

def test():
	try:
		#因为finally块中包含了return语句
		#所以下面的return语句失去了作用
		return True
	finally:
		return False

a = test()
print(a)


'''
如果python程序在执行try块、except块时遇到了return或raise语句，这两条语句都会导致该方法立即结束，那么该系统执行
这两条并不会结束该方法，而是去寻找异常处理处理流程中的finally块，如果没有找到finally块，立即执行return或者raise
方法中止；如果找到finally块，系统立即执行finally块-----只有当finally块执行完，系统才会回来执行try块、except块
里的return或raise语句；如果在finally块里也使用了return或raise等导致方法中止的语句，finally块已经中止了方法，系统
将不会跳回去执行try块、except块里的任何代码。

------------------------------------------------------ --------
尽量避免在finally块里使用return或raise等导致方法中止的语句，否则可能出现一些奇怪的现象。
'''


'''
异常处理嵌套:
异常处理的流程代码可以放在任何能执行代码的地方，因此完整的异常处理流既可被放在try块里，也可被放在except块里
还可被放在finally块里。

对于异常处理的嵌套深度没有明确的限制，但通常没有必要使用超两层的嵌套处理，使用层析太深的嵌套处理没有太大必要
而且容易降低程序的可读性。
'''

