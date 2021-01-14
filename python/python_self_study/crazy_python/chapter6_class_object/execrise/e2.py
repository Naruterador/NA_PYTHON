#coding=utf-8
'''
利用第一题的Student定义的类，定义一个列表，保存多个student对象作为通讯录属性。
程序可以通过name、email、address查询，如果找不到数据，则进行友好提示
'''

class Classroom(object):
	
		
	num = 0
	@classmethod
	def addnum(cls):
		cls.num = cls.num + 1
		
	@classmethod
	def getnum(cls):
		return cls.num
	
	def __new__(cls):
		Classroom.addnum()
		return super(Classroom,cls).__new__(cls)

class Student(Classroom):
	
	def __init__(self,name,gender,phone,address,email):
		self.name = name
		self.gender = gender
		self.phone = phone
		self.address = address
		self.email = email
	
	def __new__(cls,name,gender,phone,address,email):
		return super(Student,cls).__new__(cls)
	
	@property
	def inputname(self):
		return self.name
	
	@inputname.setter
	def inputname(self,name):
		if name.isdigit():
			print('The name can not contain number!')
		else:
			self.name = name
	
	def getgender(self):
		return self.gender
	
	def setgender(self,gender):
		if (gender == 'MALE') or (gender == 'FEMALE'):
			self.gender = gender
		else:
			print('Please input "FEMALE" or "MALE"')
	inputgender = property(getgender,setgender)
	
	def eat(self):
		pass
		
	def drink(self):
		pass
	
	def play(self):
		pass

s1 = Student('aaa','MALE','13815060645','FuMingRoad296','103258937@qq.com')
s2 = Student('bbb','FEMALE','13815060600','FuMingRoad211','183491819@qq.com')

addresslist = []

addresslist.append(s1)
addresslist.append(s2)

checkitems = input("Please input the items(name,email,address):")

k = 0
for i in addresslist:
	if checkitems == i.name or checkitems == i.email or checkitems == i.address:
		k = k + 1
	else:
		pass

if k == 1:
	print("The student is in class.")
else:
	print("The student is not in class.")
		

    
