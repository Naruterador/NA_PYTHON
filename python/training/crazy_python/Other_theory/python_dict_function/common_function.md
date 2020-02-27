####常用字典函数

1.修改或者添加字典的参数

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

如果一个键值已经存在，那么可以修改它的值
dict['Age'] = 8

如果一个键值不存在，那么可以增加
dict['School'] = "DPS School"
print （"dict['Age']: ", dict['Age']）
print （"dict['School']: ", dict['School']）


以上实例输出结果：
dict['Age']:  8
dict['School']:  DPS School


2.删除字典元素
删除一个字典用del命令，如下实例：
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键是'Name'的条目

dict.clear()     # 清空词典所有条目

del dict        # 删除词典



3.获取字典的所有键值
Python 字典keys() 函数以列表返回一个字典所有的键，以下实例展示了 keys()函数的使用方法：

dict.keys()
参数
NA。
返回值
返回一个字典所有的键。

实例:
dict = {'Name': 'Zara', 'Age': 7}
print "Value : %s" %  dict.keys()


以上实例输出结果为：
Value : ['Age', 'Name']


4.字典(Dictionary) get()方法
Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。

dict.get(key, default=None)

参数
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值。
返回值
返回指定键的值，如果值不在字典中返回默认值None。

实例:
dict = {'Name': 'Zara', 'Age': 27}
print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Sex', "Never")

以上实例输出结果为：
Value : 27
Value : Never