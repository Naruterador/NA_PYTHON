#coding=utf-8

'''
定义一个代表二维坐标系上某个点的Point类（包括x、y两个属性），为该类提供一个方法用于计算两个point之间的距离
在提供一个方法用于判断三个point组成的三角形是钝角、锐角还是直角三角形

1.需要知道计算两点之间距离的公式
'''

import math

class Point(object):
	@staticmethod
	def __new__(cls,*args):
		return super(Point,cls).__new__(cls)
	
	def __init__(self,*args):
		self.x1 = args[0]
		self.y1 = args[1]
		self.x2 = args[2]
		self.y2 = args[3]
		self.x3 = args[4]
		self.y3 = args[5]
		self.distance = 0
		self.angle = 0
	
	def __calculatedistance(self):
		self.distance = math.sqrt((self.x2 -self.x1) * (self.x2 - self.x1) + (self.y2 - self.y1) * (self.y2 - self.y1))
		
	def __calculateangle(self):
		sa = (self.x2 - self.x1) * (self.x2 - self.x1) + (self.y2 - self.y1) * (self.y2 - self.y1)
		sb = (self.x3 - self.x2) * (self.x3 - self.x2) + (self.y3 - self.y2) * (self.y3 - self.y2)
		sc = (self.x3 - self.x1) * (self.x3 - self.x1) + (self.y3 - self.y1) * (self.y3 - self.y1)
		#分别求出三条边的长度
		side1 = math.sqrt(sa)
		side2 = math.sqrt(sb)
		side3 = math.sqrt(sc)
		#求出余弦值
		pos = (sa + sb - sc)/(2 * side1 * side2)
		#余弦值转换为弧度值
		angle = math.acos(pos)
		#弧度值转为角度值
		realangle = angle / math.pi * 180
		
		self.angle = int(realangle)
	
	def __checkangle(self,angle):
		if angle > 0 and angle < 90:
			return "This is a acute angle."
		elif angle > 90 and angle < 180:
			return "This is a obtuse angle."
		elif angle == 90:
			return "This is a right angle."
		elif angle == 180:
			return "This is a flat angle."
		else:
			return "This is a line."
		   
	
	def printoutangle(self):
		self.__calculateangle()
		return self.__checkangle(self.angle)
		
	def printoutdistance(self):
		self.__calculatedistance()



p = Point(1,1,5,1,5,10) 
print(p.printoutangle())
