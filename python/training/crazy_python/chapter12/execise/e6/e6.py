#coding = utf - 8


'''
实现一个程序，当用户运行该程序时，提示用户输入一个路径。该程序会将该路径下的文件、文件夹数量统计出来。
'''



import pathlib
import os

class traverse:

	def __init__(self,path):
		self.path = pathlib.Path(path)
		self.filecount = 0
		self.directorycount = 0



	def _traverse_run(self,path):
		for i in path.iterdir():
			if os.path.isdir(i):
				self.directorycount += 1
				self._traverse_run(i)
			else:
				self.filecount += 1

	def output(self):
		self._traverse_run(self.path)
		print('Amout of the file of the directory are %d' % self.filecount)
		print('Amount of the directory of the directory are %d' % self.directorycount)


t = traverse('/Users/kingdom/Documents')
t.output()