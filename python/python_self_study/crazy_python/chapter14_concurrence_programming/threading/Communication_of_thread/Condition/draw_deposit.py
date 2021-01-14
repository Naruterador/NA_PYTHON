#coding = utf - 8

'''
程序中的存款者线程循环100次重复存款，而取钱者线程则循环100次重复取钱，存款者线程和取钱者线程分别调用
Account对象的deposit()、draw()方法来实现。主程序可以启动任意多个"存款"和"取钱"线程，可以看到所有
的"取钱"线程必须等"存款"线程存钱后才可以向下执行，而"存款"线程也必须等"取钱"后才可以向下执行。

主程序代码如下:
'''


import threading
import Account

#定义一个函数，模拟重复max次执行取钱操作
def draw_many(account,draw_amount,times):
	for i in range(times):
		account.draw(draw_amount)

#定义一个函数，模拟重复max次执行存款操作
def deposit_many(account,deposit_amount,times):
	for i in range(times):
		account.deposit(deposit_amount)

#创建一个账户
acct = Account.Account("user1",0)

#创建并启动一个"取钱"线程
threading.Thread(name = "取钱者",target=draw_many,args=(acct,800,3)).start()

#创建并启动一个"存款"线程
threading.Thread(name = "存款者甲",target=deposit_many,args=(acct,800,3)).start()
#threading.Thread(name = "存款者乙",target=deposit_many,args=(acct,800,100)).start()
#threading.Thread(name = "存款者丙",target=deposit_many,args=(acct,800,100)).start()


'''
通过这个程序我们可以看出，每当存款者向账户中存入800元之后，取钱者立即从账户中取出这笔钱。
存款完成后账户总余额是800，取钱结束后账户总余额是0.

从程序中可以看出，3个存款者线程随机地向账户中存钱，只有1个取钱者线程执行取钱操作。只有当
线程取钱后，存款者线程才可以存钱;同理，只有等存款者线程启动后，取钱者线程才可以取钱。

上面这个程序最后阻塞无法继续向下执行。这是因为3个存款者公有300次尝试存钱操作，但1个取钱者线程
只有100次尝试取钱操作，所有最后程序被阻塞！


***上面这个程序并不是死锁情况，在上面程序的情况中，因为取钱者线程已经执行结束，而存款者线程只是
在等待其他线程来取钱而已，并不是等待其他线程释放同步监视器。不要吧死锁和程序阻塞等同起来！
'''
