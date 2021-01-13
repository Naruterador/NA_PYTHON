#!/user/bin/env python3
#-*- coding:utf-8 -*-

#无异常发生时的例子:


class Test:
	def __enter__(self):
		print('__enter__() is call!')
		return self
	def dosomething(self):
		print('dosomethong!')
	def __exit__(self, exc_type, exc_value, traceback):
		print('__exit__() is call!')
		print(f'type:{exc_type}')
		print(f'value:{exc_value}')
		print(f'trace:{traceback}')
		print('__exit()__ is call!')

with Test() as sample:
	sample.dosomething()
 
'''
输出:
__enter__() is call!
dosomethong!
__exit__() is call!
type:None
value:None
trace:None
__exit()__ is call!



以上的实例Text,我们注意到他带有__enter__()/__exit__()这两个方法，当对象被实例化时，就会主动调用__enter__()方法
任务执行完成后就会调用__exit__()方法，另外，注意到，__exit__()方法是带有三个参数的(exc_type, exc_value, traceback)
依据上面的官方说明：如果上下文运行时没有异常发生，那么三个参数都将置为None, 这里三个参数由于没有发生异常，的确是置为了None, 与预期一致. 
'''