#coding = utf - 8



'''
实现一个程序，该程序是提供用户输入一个文件路径，程序读取这个可能包含手机号码的文本文件(该文件内容可能很大)
要求程序能识别出该文本文件中所有的手机号码，并将这些手机号码保存到phone.txt中。
'''


import re
import os

class fpnumber:

	def __init__(self,path):
		self.path = path
		self.p = re.compile(r"""(?:139|138|137|136|135|134|147|150|151|152|157|158|159|172|178|182|183|184|187|188|198|130|131|132|140|
							\-
							145|146|155|156|166|167|185|186|145|175|176|
							\-
							133|149|153|177|173|180|181|189|191|199)\d{8}""",re.X)


	def _identify(self,path):
		f = open('cellphonenumber.txt','r+')
		data = f.read()
		m = self.p.findall(data)
		for x in m:
			f2 = open('phone.txt','a+')
			f2.writelines(x + os.linesep)
		f2.close()

	def output(self):
		self._identify(self.path)



f = fpnumber('cellphonenumber.txt')
f.output()




