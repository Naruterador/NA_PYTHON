###使用队列(Queue)控制线程通信
    > 在queue模块下提供了几个阻塞队列，这些队列主要用于实现通信。在queue模块下主要提供了三
      个类，分别代表三种队列，它们主要区别就在于进队列、出队列的不同。关于这三个队列类的简单
      介绍如下。

      > queue.Queue(maxsize = 0):代表FIFO(先进先出)的常规队列，maxsize可以限制队列的
        大小。如果队列的大小达到队列的上限，就会加锁，再次加入元素时就会被阻塞，直到队列中
        的元素被消费。如果将maxsize设置为0或负数，则该队列的大小就是无限制的。
      > queue.LifoQueue(maxsize = 0):代表LIFO(后进先出)队列，与Queue的区别就是出队列
        的顺序不同
      > PriorityQueue(maxsize = 0):代表优先级队列，优先级最小的元素先出队列。这三个队列
        类的属性和方法基本相同，它们都提供如下属性和方法。
      > Queue.qsize():返回队列的实际大小，也就是该队列中包含几个元素
      > Queue.empty():判断队列是否空
      > Queue.full():判断队列是否已满
      > Queue.put(item,block=True,timeout=None):向队列中放入元素。如果队列已满，且
        block参数为True(阻塞)，当前线程被阻塞，timeout指定阻塞时间，如果将timeout设置
        为None,则代表一直阻塞，直到该队列的元素被消费；如果队列已满，且block参数为False
        (不阻塞)，则直接引发queue.FULL异常
      > Queue.put_nowait(item):向队列中放入元素，不阻塞。相当于在上一个方法中将block
        参数设置为False
      > Queue.get(item,block=True,time=None):从队列中取出元素(消费元素)。如果队列
        已经满，且block参数为True(阻塞)，当前线程被阻塞，timeout指定阻塞时间，如果将
        timeout设置为None,则代表一直阻塞，直到有元素被放入队列中;如果队列已空，且block
        参数为False(不阻塞)，则直接引发queue.EMPTY异常。
      > Queue.get_nowait(item):从队列中取出元素，不阻塞。相当于在上一个方法中将block
        参数设置为False