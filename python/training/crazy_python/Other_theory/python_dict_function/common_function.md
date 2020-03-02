####常用字典函数
<pre>
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


5.函数把字典dict2的键/值对更新到dict里
dict.update(dict2)

参数
dict2 -- 添加到指定字典dict里的字典。
返回值
该方法没有任何返回值。

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print "Value : %s" %  dict

以上实例输出结果为：
Value : {'Age': 7, 'Name': 'Zara', 'Sex': 'female'}



6.items() 函数以列表返回可遍历的(键, 值) 元组数组
dict.items()

参数
NA。
返回值
返回可遍历的(键, 值) 元组数组。

实例:
dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print "字典值 : %s" %  dict.items()
 
#遍历字典列表
for key,values in  dict.items():
    print key,values

以上实例输出结果为：
字典值 : [('Google', 'www.google.com'), ('taobao', 'www.taobao.com'), ('Runoob', 'www.runoob.com')]
Google www.google.com
taobao www.taobao.com
Runoob www.runoob.com


















</pre>