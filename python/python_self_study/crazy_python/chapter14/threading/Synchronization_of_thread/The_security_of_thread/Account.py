#coding = utf - 8



'''

按照上面的流畅编写取款程序，并使用两个线程来模拟模拟两个人使用同一个账户并发取钱操作。
此处忽略检查账户和密码的操作，仅仅模拟后面三步操作。

下面代码先定义一个账户类，该账户类封装了账户编号和余额连个成员变量。
'''

class Account(object):
	#定义构造器
	def __init__(self,account_no,balance):
		#封装账号编号和账户余额两个成员变量
		self.account_no = account_no
		self.balance = balance