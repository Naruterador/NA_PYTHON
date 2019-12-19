#coding = utf - 8


'''
线程同步

多线程编程是一件很有趣的事情，它很容易突然出现“错误情况”，这是由系统的线程调度具有
一定的随机性造成的。不过，即使程序偶然出现问题，那也是由于编程不当引起的。当使用多个
线程来访问同一个数据时，很容易“偶然”出现线程安全问题。


线程安全问题

关于线程安全问题，有一个经典问题——————从银行取钱问题。

从银行取钱的基本流程基本上可以分为如下几个步骤:
1.用户输入账户、密码、系统判断用户账户、密码是否匹配。
2.用户输入取款金额。
3.系统判断账户余额是否大于取款金额。
4.如果余额大于取款金额，则取款成功；如果余额小于取款金额，则取款失败。
一般来说，这个流程是没有任何问题的。但一旦将这个流程放在多线程并发的场景下
就有可能出现问题。这边说是有可能出问题，并不说是一定。也许运行了程序一百万次都没问题
但是没出现问题不等于没问题。
'''