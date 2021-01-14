#!/user/bin/env python3
#-*- coding:utf - 8 -*-

#有异常发生时，不再抛出异常的例子：



class Test:
	def __enter__(self):
		print('__enter__() is call!')
		return self
	def dosomething(self):
		x = 1/0
		print('dosomethong!')
	def __exit__(self, exc_type, exc_value, traceback):
		print('__exit__() is call!')
		print(f'type:{exc_type}')
		print(f'value:{exc_value}')
		print(f'trace:{traceback}')
		print('__exit()__ is call!')
		return True
with Test() as sample:
	sample.dosomething()



'''
从结果看，异常抛出被抑制了，符合预期。
'''