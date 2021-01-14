#coding = utf - 8



'''
下面程序示范了使用apply_async()方法启动进程
'''


import multiprocessing
import time 
import os 

def action(name='default'):
	print('(%s)进程正在执行，参数为: %s' % (os.getpid(),name))
	time.sleep(3)

if __name__ == '__main__':
	#创建包含4个进程的进程池:
	pool = multiprocessing.Pool(processes=4)
	#将action分3次提交给进程池
	pool.apply_async(action)
	pool.apply_async(action,args=('位置参数',))
	pool.apply_async(action,kwds={'name':'关键字参数'})
	pool.close()
	pool.join()

'''
上面程序中pool = multiprocessing.Pool(processes=4)代码创建了一个进程池
接下来代码:
	pool.apply_async(action)
	pool.apply_async(action,args=('位置参数',))
	pool.apply_async(action,kwds={'name':'关键字参数'})
都负责将action提交给进程池，只是每次提交时指定参数的方式不同。


程序输出结果为:
(21101)进程正在执行，参数为: default
(21102)进程正在执行，参数为: 位置参数
(21103)进程正在执行，参数为: 关键字参数

从上面的输出结果可以看出，程序分别使用3个进程来执行action任务。
从上面的程序可以看出，进程池同样实现了上下文管理协议，因此程序可以使用with
子语句来管理进程池，这样就可以避免程序主动关闭进程池。

'''