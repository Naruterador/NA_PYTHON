#coding = utf - 8 



'''
下面程序示范了使用map()方法来启动进程
'''


import multiprocessing
import time
import os


#定义了一个准备作为进程任务的函数
def action(max):
	my_sum = 0
	for i in range(max):
		print('(%s)进程正在执行:%d' % (os.getpid(),i))
		my_sum += i
	return my_sum

if __name__ == '__main__':
	#创建一个含有4个进程的进程池
	with multiprocessing.Pool(processes=4) as pool:
		#使用进程执行map计算
		#后面元组由3个元素，因此程序启动3个进程来执行action函数
		results = pool.map(action,(50,100,150))
		print('-----------------')
		for r in results:
			print(r)


'''
运行上面的程序，可以看到程序启动3个进程来执行action函数，程序最后输出0~50,0~100
0~150累加的结果

其实该程序与前面介绍的线程池的map()方法时所用的实力程序几乎一样。事实就是如此，只不过前面的
程序使用了更轻量级的线程来实现并发，而此处则使用进程来实现并发。这两种方式殊途同归，但相比之下
使用线程会有更好的性能，因此一般推荐使用多线程来实现并发。
'''
