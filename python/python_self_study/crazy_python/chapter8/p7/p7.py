#conding = utf-8

'''
程序可以通过判断该属性（或方法）是否包含__call__属性来确定它是否可调用。
'''

class User(object):
	def __init__(self,name,passwd):
		self.name = name
		self.passwd = passwd
	def vaildLogin(self):
		print('验证%s的登陆' % self.name)

u = User('crazyit','leegang')

#判断u.name是否包含__call__方法，即判断它是否可调用
print(hasattr(u.name,'__call__'))    #False
#判断u.passwd是否包含__call__方法，即判断它是否可调用
print(hasattr(u.passwd,'__call__'))  #False
#判断u.vaildLogin是否包含__call__方法，即判断它是否可调用
print(hasattr(u.vaildLogin,'__call__'))  #Trure