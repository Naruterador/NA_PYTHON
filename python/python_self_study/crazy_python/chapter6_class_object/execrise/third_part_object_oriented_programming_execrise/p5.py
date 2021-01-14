#coding=utf-8
'''
房子 (House) 有 户型、总面积 和 家具名称列表

新房子没有任何的家具
家具 (HouseItem) 有 名字 和 占地面积，其中

席梦思 (bed) 占地 4 平米
衣柜 (chest) 占地 2 平米
餐桌 (table) 占地 1.5 平米
将以上三件 家具 添加 到 房子 中
打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

'''

class HouseItem:

	def __init__(self,name,area):
		self.name = name
		self.area = area

	def __str__(self):
		return (name," area is ",area)

ie1 = HouseItem("bed",4)
ie2 = HouseItem("chest",2)
ie3 = HouseItem("table",1.5)
ie4 = HouseItem("warehoues",1000)





class House:
	def __init__(self,house_type,area,free_area):
		self.house_type = house_type
		self.area = area
		self.free_area = free_area
		self.item_list = []
	
	def additem(self,itemname,itemarea):
		if itemarea > self.free_area:
			print ("%s area is too large to add into the house" % itemname)
			return
		self.item_list.append(itemname)
		self.free_area = self.free_area - itemarea

	def __str__(self):
		return ("House_type:%s total_area:%s free_area:%s item_list:%s" % (self.house_type,self.area,self.free_area,self.item_list)) 

h1 = House("small",100,100)
h1.additem(ie1.name,ie1.area)
h1.additem(ie2.name,ie2.area)
h1.additem(ie3.name,ie3.area)
h1.additem(ie4.name,ie4.area)
print(h1)