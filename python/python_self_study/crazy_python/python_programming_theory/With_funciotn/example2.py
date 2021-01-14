#!/user/bin/env python3
#-*- coding:utf-8 -*-



'''
有异常发生时，会抛出异常的例子：
以下例子在上面稍做了一些修改，让运行时产生异常，看看这三个参数的赋值情况：
'''


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
		# return True
 
with Test() as sample:
	sample.dosomething()



'''
从结果可以看出, 在执行到dosomethong时就发生了异常，然后将异常传给了__exit__(), 依据上面的官方说明：如果有异常发生，并且该方法希望抑制异常（即阻止它被传播）
则它应该返回True。否则，异常将在退出该方法时正常处理。当前__exit__并没有写明返回True，故会抛出异常，也是合理的，但是正常来讲，程序应该是不希望它抛出异常的
这也是调用者的职责，我们将再次修改__exit__, 将其返回设置为True, 
'''