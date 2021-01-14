#coding=utf-8
'''
枚举也是类，因此枚举也可以定义构造器。为枚举定义构造器之后，在定义枚举实例时必须为构造器参数设置值。
'''

import enum

class Gender(enum.Enum):
	MALE = '男','阳刚之力'
	FEMALE = '女','阴柔之美'

	def __init__(self,cn_name,desc):
		self._cn_name = cn_name
		self._desc = desc

	@property
	def desc(self):
		return self._desc

	@property
	def cn_name(self):
		return self._cn_name


#访问FEMALE的name
print('FEMALE的NAME:',Gender.FEMALE.name)

#访问FEMALE的value
print('FEMALE的VALUE:',Gender.FEMALE.value)

#访问自定义的cn_name属性
print('FEMALE的cn_name:',Gender.FEMALE.cn_name)

#访问自定义的desc属性
print('FEMALE的desc:',Gender.FEMALE.desc)

