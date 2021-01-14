#coding = utf - 8



#下面以普通的Queue为例介绍阻塞队列的功能和用法。首先用一个最简单的程序来测试Queue的put()和get()方法



import queue


#定义一个长度为2的阻塞队列

bq = queue.Queue(2)
bq.put("Python")
bq.put("Python")
print("11111111")
bq.put("Python")   #1代码:由于队列申明的时候长度为2，这里在队列中加入了第三个值，队列阻塞
bq.get(timeout=1)
print("22222222")



'''
上面程序预先定义了一个大小为2的Queue,程序先向该队列中放入两个元素，此时队列还没有满，两个元素
都可以被放入。当程序试图放入第三个元素时，如果使用put()方法尝试放入元素将会阻塞线程，如上面
程序的#1代码处。
'''