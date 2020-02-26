###python常用列表操作函数

1.append()
append() 方法用于在列表末尾添加新的对象。

list.append(obj)

参数
obj -- 添加到列表末尾的对象。
返回值
该方法无返回值，但是会修改原来的列表。

实例:
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)

以上实例输出结果如下：
更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']



2.count()
Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

str.count(sub, start= 0,end=len(string))
参数
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
返回值
该方法返回子字符串在字符串中出现的次数。


实例1:
str = "this is string example....wow!!!";
sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)


以上实例输出结果如下：
str.count(sub, 4, 40) :  2
str.count(sub) :  1


3.extend()
extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。

list.extend(seq)

参数
seq -- 元素列表。
返回值
该方法没有返回值，但会在已存在的列表中添加新的列表内容。

实例1:
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print "Extended List : ", aList ;

以上实例输出结果如下：
Extended List :  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']



4.insert()
insert() 函数用于将指定对象插入列表的指定位置。

list.insert(index, obj)

参数
index -- 对象 obj 需要插入的索引位置。
obj -- 要插入列表中的对象。
返回值
该方法没有返回值，但会在列表指定位置插入对象。

实例1:
aList = [123, 'xyz', 'zara', 'abc']
aList.insert(3, 2009)
print "Final List : ", aList

以上实例输出结果如下：
Final List : [123, 'xyz', 'zara', 2009, 'abc']




5.remove()
remove() 函数用于移除列表中某个值的第一个匹配项。

list.remove(obj)
参数
obj -- 列表中要移除的对象。
返回值
该方法没有返回值但是会移除列表中的某个值的第一个匹配项。

实例1:
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.remove('xyz');
print "List : ", aList;
aList.remove('abc');
print "List : ", aList;

以上实例输出结果如下：
List :  [123, 'zara', 'abc', 'xyz']
List :  [123, 'zara', 'xyz']


6.删除元素 del list[index]
如果要删除某个指定索引index的元素，那么可以采用：
   del list[index]

例如：
aList = [123, 'xyz', 'zara', 'abc']
del aList[2]
print(aList)
结果：
[123, 'xyz', 'abc']


7. pop()
pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

list.pop([index=-1])

参数
obj -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
返回值
该方法返回从列表中移除的元素对象。

实例:
list1 = ['Google', 'Runoob', 'Taobao']
list_pop=list1.pop(1)
print "删除的项为 :", list_pop
print "列表现在为 : ", list1

以上实例输出结果如下：
删除的项为 : Runoob
列表现在为 :  ['Google', 'Taobao']



8.reverse()
reverse() 函数用于反向列表中元素。

list.reverse()

参数
NA。
返回值
该方法没有返回值，但是会对列表的元素进行反向排序。

实例:
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print "List : ", aList

以上实例输出结果如下：
List :  ['xyz', 'abc', 'zara', 'xyz', 123]