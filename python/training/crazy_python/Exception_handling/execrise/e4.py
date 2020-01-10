#coding=utf-8

'''
提示用户输入x1,y1,x2,y2,x3,y3六个数值，分别代表三个点的坐标，程序判断这三个点是否在同一条直线上。
要求:使用异常处理机制处理用户输入的各种错误情况，如果三个点不在同一条直线上，则程序出现异常。
'''

import math

class SelfException(Exception):
	pass


inputcordinate = input("Please type the 6 pointer:")

lista = inputcordinate.split(",")

x1 = int(lista[0])
y1 = int(lista[1])

x2 = int(lista[2])
y2 = int(lista[3])

x3 = int(lista[4])
y3 = int(lista[5])

try:
	sa = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
	sb = (x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)
	sc = (x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1)
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
		
	angle = int(realangle)

	if angle == 180 or angle == 0:
		print("三个点在一条直线上")
	else:
		raise SelfException("三个点不在一条直线上！")
		
except SelfException as ae:
	print("异常",ae)