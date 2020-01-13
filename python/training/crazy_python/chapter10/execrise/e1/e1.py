#coding = utf - 8



'''
提示用户输入自己的名字、年龄、身高、并将该用户的信息以JSON格式保存在文件中。再写一个程序读取刚刚保存的JSON文件
恢复用户输入的信息。
'''

import json

class JSONSandJSONR:

	def __init__(self,name,age,height):
		self.name = name
		self.age = age
		self.height = height



	def _converttoJSON(self):
		information = {'name':self.name,'Age':self.age,'Height':self.height}
		f = open('information.json','w+')
		s = json.dump(information,f)
		print(s)


	def _reconvertopython(self):
		f = open('information.json','r+')
		data = f.read()
		p = json.loads(data)
		print(p)

	def input(self):
		self._converttoJSON()

	def output(self):
		self._reconvertopython()



j = JSONSandJSONR('Rich',15,175)
j.output()