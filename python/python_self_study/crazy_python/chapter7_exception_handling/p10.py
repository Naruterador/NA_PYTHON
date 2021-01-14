#coding=utf-8

'''
except和raise同时使用:

在实际应用中对异常可能需要更复杂的处理方式--当一个异常出现时，单靠某个方法无法完全处理该异常，必须由几个方法协作才能完全处理该异常。也就
是说，在异常出现的当前方法中，程序只对异常进行部分处理还有些处理需要在该方法的调用者中才能完成，所以应该再次引发异常，让该方法的调用者也能捕获到异常。

为了实现这种通过多个方法协作处理同一个异常的情形，可以在except块中结合raise语句来完成.
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
			raise AuctionException("竞拍价格必须是数值，不能包含其他字符！")
		if self.init_price > d:
			raise AuctionException("竞拍价格比起拍价低，不允许竞拍！")
		initprice = d

def main():
	at = AuctionTest(20.4)
	try:
		at.bid("df")
	except AuctionException as ae:
		#再次捕获到bid()方法中的异常，并对该异常进行处理
		print("main函数捕获的异常:",ae)
main()


'''
上面的程序中，except块捕获到异常后，系统打印了该异常的字符串信息，接着引发了一个AuctionException异常，通知该方法的调用者再次
处理该AuctionException异常。所以程序中的main()函数，也就是bid()方法的调用者还可以再次捕获AuctionException异常，并将该异常
的详细信息打印出来。

这种except和raise结合使用的情况在实际应用中非常常用。实际应用对异常的处理通常分成两部分:
1.应用后台需要通过日志来记录异常发生的详细情况；
2.应该还需要根据异常向应用使用者传达某种提示。
3.在这种情况下，所有异常都需要两个方法共同完成，也就必须将except和raise结合使用。

如果程序需要将原始异常的详细信息直接传播出去，Python也允许用自定义异常对原始异常进行包装，代码形式如下:
		raise AuctionException(e)
'''