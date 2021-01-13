#coding = utf - 8

'''
自定义一个二维坐标系上某个点的Point类(包括X、Y两个属性)，为Point类提
自定义的减法运算支持，计算结果返回两点之间距离
'''
#调用数学模块
import math

#创建一个Point类
class Point(object):
	def __init__(self,x1,y1):
		#横坐标x1
		self.x1 = x1
		#纵坐标y1
		self.y1 = y1

	#获取x1和y1的值
	def getpoint(self):
		return self.x1,self.y1

	#设置x1和y1的值
	def setpoint(self,val):
		self.x1,self.y1 = val

	#使用property设置val的值
	val = property(getpoint,setpoint)


	def __sub__(self,other):
		#要求参与减法运算的另外一个类必须是Point
		if not isinstance(other,Point):
			raise TypeError('-运算要求的目标也必须是Point类的实例')
		#通过公式计算两点之间距离的数学表达式	
		a = ((self.x1 - other.x1) * (self.x1 - other.x1)) + ((self.y1 - other.y1) * (self.y1 - other.y1))
		ab = math.sqrt(a)
		return ab

p1 = Point(1,10)
p2 = Point(2,10)

p3 = p1 - p2

print(p3)