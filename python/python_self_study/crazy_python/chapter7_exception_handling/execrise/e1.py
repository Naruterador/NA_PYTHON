#coding=utf-8

'''
提示用户输入一个N，表示用户接下来要输入N个字符串，程序尝试将用户输入的每一个字符串用空格分割成两个整数，并结算这两个整数整除的结果。要求:
使用异常处理机制来处理用户输入的各种错误情况，并提示用户重新输入。
'''


class AuctionException(Exception):
	pass

class exceptiontest1(object):
	def __init__(self,userinput):
		self.userinput = userinput

	def __new__(cls,userinput):
		return super().__new__(cls)

	def __splitstr(self):
		lista = self.userinput.split(' ')
		return lista

	def check1(self):
		c = 0
		lista = self.__splitstr()
		if len(lista) == 2:
			c = int(lista[0]) / int(lista[1])
		return c

def main():
	while(1):
		inputstr = input('Please input 2 numbers split with space:')
		if inputstr:
			et = exceptiontest1(inputstr)
			try:
				print(et.check1())
				break
			except Exception as e:
				print(e)
				continue
		else:
			continue
main()