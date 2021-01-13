#coding=utf-8

'''
raise不需要参数

在使用raise语句时可以不带参数，此时raise语句处于except块中，它将会自动引发当前上下文激活的异常；否则，通常默认引发RuntimeError异常
'''


class AuctionException(Exception):
	pass

class AuctionTest(object):
	def __init__(self,init_price):
		self.init_price = init_price

	def bid(self,bid_price):
		d = 0.0
		try:
			d = float(bid_price)
		except Exception as e:
			#此处只是简单地打印异常信息
			print("转换出异常:",e)
			#再次引发自定义异常
			raise 
		if self.init_price > d:
			raise AuctionException("竞拍价格比起拍价低，不允许竞拍！")
		initprice = d

def main():
	at = AuctionTest(20.4)
	try:
		at.bid("df")
	except Exception as ae:
		#再次捕获到bid()方法中的异常，并对该异常进行处理
		print("main函数捕获的异常:",type(ae))
main()


'''
输出结果:
转换出异常: could not convert string to float: 'df'
main函数捕获的异常: <class 'ValueError'>

丛输出结果来看，此时main()函数再次捕获了ValueError--它就是在bid方法中except块所捕获的原始异常。
'''

