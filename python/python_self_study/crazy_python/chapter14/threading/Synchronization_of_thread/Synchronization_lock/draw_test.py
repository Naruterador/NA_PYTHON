#coding = utf - 8

import threading
import Account


'''
下面程序创建了并启动了两个取钱线程
'''

#定义一个函数来模拟取钱操作
def draw(account,draw_amount):
	#直接调用Account对象的draw()方法来执行取钱操作
	account.draw(draw_amount)


#创建一个账户
acct = Account.Account('user1',1000)
#使用两个线程模拟从同一个账户中取钱
threading.Thread(name = '甲',target = draw,args=(acct,800)).start()
threading.Thread(name = '乙',target = draw,args=(acct,800)).start()


'''
上面程序中代表线程执行体的draw()函数无需自己实现取钱操作，而是直接调用account
的draw()方法来执行取钱操作。由于draw()方法已经使用RLock对象实现了线程安全，因
此上面程序就不会出现线程安全问题



***在Account中定义draw()方法，而不是直接在线程执行体函数中实现取钱逻辑，这种做法
更符合面向对象规则。在面向对象中有一种流行的设计方式:Domain Driven Design(领域
驱动设计(DDD)),这种方式认为每个类都应该是完备的领域对象，例如Account代表用户账户
应该提供用户账户的相关方法;通过draw()方法来执行取钱操作(实际上还应该提供transfer()
等方法来完成转账操作)，而不是直接将setBalance()方法暴露出来任人操作，这样才可以更好地
保证Account对象的完整性和一致性。


可变类的线程安全是以降低程序运行的效率作为代价的，为了减少线程安全锁带来的负面影响
程序可以采用如下策略
1.不要对线程安全类的所有方法都进行同步，只对那些会改变竞争资源(竞争资源也就是共享
  资源)的方法进行同步。例如，上面Account类中的account_no实例变量就无需同步，所以
  程序只对draw()方法进行了同步控制。
2.如果可变类有两种运行环境:单线程环境和多线程环境，则应该为该可变类提供两个版本即线
  程不安全版本和线程安全版本。在单线程环境中使用线程不安全版本以保证性能，在多线程
  环境中使用线程安全版本


'''