#coding = utf - 8


'''
实现一个程序，该程序提示用户运行该程序一个路径。该程序会将该路径下(及其子目录下)的所有文件列出来
'''

import pathlib
import os

class traverse:

	def __init__(self,path):
		self.path = pathlib.Path(path)



	def _traverse_run(self,path):
		for i in path.iterdir():
			if os.path.isdir(i):
				self._traverse_run(i)
			else:
				print(i)

	def output(self):
		self._traverse_run(self.path)

t = traverse('/opt')
t.output()