'''
dict.item():
以列表返回可便利的键、值
'''
import time

myD = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g'}

for key,value in dict.items(myD):
	print(key,value)
	time.sleep(1)    #暂停一秒