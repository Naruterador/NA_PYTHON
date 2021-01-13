#-*- coding:utf-8 -*-



'''
下面程序示范了使用sched.scheduler来执行任务调度
'''


import sched,time,threading


#定义线程任务调度器
s = sched.scheduler()

#定义被调度的函数
def print_time(name='default'):
	print("%s 的时间 %s" % (name,time.ctime()))

print('主线程:',time.ctime())
#指定10秒后执行print_time()函数
s.enter(10,1,print_time)
#指定5秒执行print_time()函数，优先级为2
s.enter(5,2,print_time,argument=('位置参数2',))
#指定5s后执行print_time()函数，优先级为1
s.enter(5,1,print_time,kwargs={'name':'关键字参数'})
#执行调度的任务
s.run()
print('主线程:',time.ctime())


'''
s.enter(10,1,print_time)指定10秒后执行print_time()函数
本次调度没有为该函数分配参数;

s.enter(5,2,print_time,argument=('位置参数',))指定5秒后调度print_time()函数
本次调度使用位置参数的形式为该函数传入参数;

代码s.enter(5,1,print_time,kwargs={'name':'关键字参数'})指定5秒后调度
print_time()函数，本次调度使用关键字参数的形式为该函数传入参数。

上面程序运行后，将会看到程序在5秒后执行来两次print_time()函数，其中传入关键字参数
的函数先执行(它的优先级更高)，10秒后执行一次print_time()函数。

程序输出结果如下:
主线程: Mon Dec 23 11:10:53 2019
位置参数 的时间 Mon Dec 23 11:10:58 2019
关键字参数 的时间 Mon Dec 23 11:10:58 2019
default 的时间 Mon Dec 23 11:11:03 2019
主线程: Mon Dec 23 11:11:03 2019

'''