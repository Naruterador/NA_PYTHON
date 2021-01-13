#-*- coding:utf-8 -*-


'''
如果程序想要取消Timer调度，则可调用Timer对象的cancel()函数。
例如，如下程序每1秒输出一次当前时间。
'''


from threading import Timer
import time



#定义总共输出几次的计数器
count = 0

def print_time():
	print("当前时间: %s" % time.ctime())
	global t,count
	count += 1
	#如果count小于10，开始下一次调度
	if count < 10:
		t = Timer(1,print_time)
		t.start()

#指定1秒后执行pring_time()函数
t = Timer(1,print_time)
t.start()



'''
上面程序开始运行后，程序控制1秒后执行print_time()函数。print_time()函数中的代码:
if count < 10:
		t = Timer(1,print_time)
		t.start()
判断:如果count小于10，程序再次使用Timer调度1秒后执行print_timer()函数，这样
就可以控制print_time()函数多次重复执行。

上面程序只有当count小于10时才会使用Timer调度1秒后执行print_time()函数，因此
上面的函数只会重复执行10次。
'''