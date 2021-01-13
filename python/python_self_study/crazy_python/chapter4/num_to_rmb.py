#coding=utf-8

'''
将一个浮点数转换成人名币读法的字符串。实现这个函数的思路是，首先吧这个浮点数分成整数部分和小数部分。提取整数部分（直接将浮点数强转成整数即可）
再使用浮点数减去整数就可以得到这个浮点数的小数部分。

小数部分处理：直接保留两位数字，转换成几角几分

整数部分处理：以中国数字记数的习惯，4位一节，一个4位的数字可被转成几千几百几十几，如果这节4位数字出现在1-4位，则后面添加单位“元”，如果这节数字
出现在5-8位，则后面添加单位“万”，如果这节数字出现在9-12位，则后面添加单位“亿”；多余十二位就暂不考虑了。

程序的关键就是把一个4位的数字字符串转换成中文读法。


'''
import decimal


class Numtormb(object):

	def __init__(self,num):
		self.num = num
		self.integer = 0
		self.fraction = 0
		self.strfloat = ""
		self.han_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
		self.unit_list = ['拾','百','千']

	def __divide(self):
		self.integer = int(self.num)
		self.fraction = self.num - self.integer


	def __four_integer_convert(self,integer):
		result = ''
		strinteger = str(integer)
		num_len = len(strinteger)


        #两位数处理
		for i in range(num_len):
			num = int(strinteger[i])
			if num_len <= 2:
				if num_len < 2: 
					result = self.han_list[num]
				elif num_len == 2 and int(self.integer) == 10:
					result = self.unit_list[0]
				else:
					result = result + self.han_list[num] + self.unit_list[0]
		#三位数处理
			elif i != num_len - 1 and num != 0:
				result = result + self.han_list[num] + self.unit_list[num_len - 2 - i]
			else:
				if (int(strinteger[i])) == 0 and (int(strinteger[i - 1])) == 0 and (int(strinteger[num_len - 1])) == 0:
					pass
				elif int(strinteger[i]) == 0 and int(strinteger[i - 1]) == 0 and i == num_len - 1:
					pass
				elif int(strinteger[i]) == 0 and int(strinteger[i - 1]) == 0 and (i != num_len - 1):
					pass
				elif (int(strinteger[i])) == 0 and (int(strinteger[num_len - 1])) != 0:
					result = result + self.han_list[num]
				elif ((int(strinteger[i - 1])) == 0) and (int(strinteger[num_len - 1])) != 0:
					result = result + self.han_list[num]
				elif int(strinteger[i]) != 0:
					result = result + self.han_list[num]

		if((len(result) == 4) and (num_len == 2)):
			return result[0:3]
		else:
			return result


	def __connect_num(self):
	
		strinteger = str(self.integer)
		result = ''
		if len(strinteger) <= 4:
			result = self.__four_integer_convert(self.integer)
			return result + '元'

		if len(strinteger) == 5:
			if(int(strinteger[1]) == 0 or int(strinteger[2]) == 0 or int(strinteger[3]) == 0) and int(strinteger[4]) != 0:
				result = self.__four_integer_convert(int(strinteger[:-4])) + '万'+ '零' + self.__four_integer_convert(int(strinteger[-4:]))
			elif (int(strinteger[1]) == 0) and int(strinteger[4]) == 0:
				result = self.__four_integer_convert(int(strinteger[:-4])) + '万'+ '零' + self.__four_integer_convert(int(strinteger[-4:]))
			else:
				result = self.__four_integer_convert(int(strinteger[:-4])) + '万' + self.__four_integer_convert(int(strinteger[-4:]))

			if len(result) == 3:
				return result[0:2]
			if len(result) == 6 and int(strinteger[4]) == 0:
				return result[0:5]
			else:
				return result 

		if len(strinteger) == 6:
			pass

		if len(strinteger) == 7:
			pass

		if len(strinteger) == 8:
			pass

		if len(strinteger) == 9:
			pass

		if len(strinteger) == 10:
			pass

		if len(strinteger) == 11:
			pass

		if len(strinteger) == 12:
			pass



	def outputform(self):
		self.__divide()
		return self.__connect_num()



d1 = Numtormb(10101)
print(d1.outputform())










