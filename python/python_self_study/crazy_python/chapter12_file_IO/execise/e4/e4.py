#coding = utf - 8




'''
实现一个程序，该程序提示用户输入一个目录，程序递归读取该目录及其子目录下所有能识别的文本文件
要求程序能识别出所有文件中的所有手机号码，并将这些手机号码保存到phone.txt文件中。
'''

import os 
import pathlib
import re


class fpnumber:

	def __init__(self,path):
		self.path = pathlib.Path(path)
		self.p = re.compile(r"""(?:139|138|137|136|135|134|147|150|151|152|157|158|159|172|178|182|183|184|187|188|198|130|131|132|140|
							\-
							145|146|155|156|166|167|185|186|145|175|176|
							\-
							133|149|153|177|173|180|181|189|191|199)\d{8}""",re.X)


	def _recursionf(self,path):
		for x in path.iterdir():
			if os.path.isdir(x):
				self._recursionf(x)
			else:
				filename = os.path.basename(x)
				if filename.endswith(".txt"):
					f1 = open(x,'r+')
					data = f1.read()
					f1.close()
					m = self.p.findall(data)
					for i in m:
						f2 = open('./phone.txt','a+')
						f2.writelines(i + os.linesep)
					f2.close()


	def output(self):
		self._recursionf(self.path)


f = fpnumber('./')
f.output()
1
