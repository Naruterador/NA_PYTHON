#coding=utf-8
'''
如果要定义更复杂的枚举，则可通过继承enum来派生枚举类，在这种方式下程序就可以枚举额外定义方法了。
'''


import enum

class Orientation(enum.Enum):
	EAST = '东'
	SOUTH = '南'
	WEST = '西'
	NORTH = '北'

	def info(self):
		print('这是一个代表方向【%s】的枚举 ' % self.value)

print(Orientation.SOUTH)
print(Orientation.SOUTH.value)


#通过枚举变量名访问枚举
print(Orientation['WEST'])
#通过枚举值来访问枚举
print(Orientation('南'))
#调用枚举的info()方法print(name,'=>',member,',',member.value)
Orientation.EAST.info()
#遍历Orientation枚举的所有成员
for name,member in Orientation.__members__.items():
	print(name,'=>',member,',',member.value)
