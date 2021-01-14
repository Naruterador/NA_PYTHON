#coding = utf - 8 

'''
billing模块文件的内容:
'''

class Item(object):
	'定义代表商品的类'
	def __init__(self,price):
		self.price = price
	def __repr__(self):
		return 'Item[price=%g]' % self.price

