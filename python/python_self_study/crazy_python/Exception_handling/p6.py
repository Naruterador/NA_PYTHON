#coding=utf-8
'''
使用finally回收资源
有些时候，程序在try块里打开了一些物理物资（例如数据库连接、网络连接和磁盘文件等），这些物理资源都必须被回收。

____________________________________________________________________________________________
Python垃圾回收机制不会回收任何物理资源，只能回收堆内存中对象所占用的内存。
'''


'''
为了保证一定能回收在try块中的打开的物资资源，异常处理机制提供了finally块。不管try块中的代码是否出现异常
不管哪一个except块被执行，甚至在try块或except块中执行了return语句，finally块总会被执行。



python完整的异常处理语法结构如下：
try:
	#code
except SubException as e:
	#异常处理块1
	...
except SubException as e:
	#异常处理块2
	...
...
else:
	#正常处理块
finally:
	#资源回收块
	...

'''

import os

def test():
	fis = None
	try:
		fis = open('a.txt')
		return
	except OSError as e:
		print(e.strerror)

	#return
    #os.exit(1)

	finally:
		if fis is not None:
			try:
				#关闭资源
				fis.close()
			except OSError as ioe:
				print(ioe.strerror)
		print('执行finally块里的资源回收！')
test()


'''
通通常情况下，方法执行到return语句，程序将会立即结束该方法，但是现在不会了，虽然return语句也强制方法结束但
一定会先执行finally块的代码

os.exit(1)语句是用来退出python解释器的，则finally将失去执行的机会。

'''
