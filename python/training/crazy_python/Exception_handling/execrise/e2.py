#coding=utf-8

'''
提示用户输入一个整数，如果用户输入的整数是奇数，则输出"有趣";如果用户输入的整数
是偶数，且在2~5之间，则打印"没意思";如果用户输入的整数偶数，且在6~20之间，则输出"有趣";
如果输入的整数是其他偶数，则打印"没意思"。要求:使用异常处理机制来处理用户输入的各种错误情况。
'''

class SelfException(Exception):
	pass


class NumberTest(object):

	def __init__(self,init_num):
		self.init_num = init_num

	def checknum(self):
		try:
			self.init_num = int(self.init_num)
			if self.init_num % 2 != 0:
				return '有趣'
			elif self.init_num % 2 == 0 and self.init_num >= 2 and self.init_num <= 5:
				return '没意思'
			elif self.init_num % 2 == 0 and self.init_num >= 6 and self.init_num <= 20:
				return '有趣'
			elif self.init_num % 2 == 0:
				return "没意思"
		except Exception as e:
			print('程序出现异常',e)
			raise SelfException('请输入一个整数')

def main():
	intnum = input("Please type a number:")
	try:
		if intnum:
			n1 = NumberTest(intnum)
			print(n1.checknum())
	except SelfException as ae:
		print("main函数问题:",ae)

main()




