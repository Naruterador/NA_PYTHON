1.len()      获取字符串长度

2.字符串去掉空格函数strip()
  Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
	注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
  实例(Python 2.0+):
	str = "00000003210Runoob01230000000"; 
	print str.strip( '0' );  # 去除首尾字符 0
 
	str2 = "   Runoob      ";   # 去除首尾空格
	print str2.strip();
  
  以上实例输出结果如下：
    3210Runoob0123
    Runoob


3.list.append(obj)
append() 方法用于在列表末尾添加新的对象。
返回值
该方法无返回值，但是会修改原来的列表。

实例
以下实例展示了 append()函数的使用方法：
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)

以上实例输出结果如下：
更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']


4.字符串转大小写函数
格式： s.upper() 
作用：返回一个字符串，把s中的所有小写转为大写
格式： s.lower()
功能：返回一个字符串，把s中所有大写字母转为小写


5.字符串查找函数find()
Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
str.find(str, beg=0, end=len(string))
参数
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。
返回值
如果包含子字符串返回开始的索引值，否则返回-1。

实例1:
str1 = "this is string example....wow!!!";
str2 = "exam";
 
print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);

以上实例输出结果如下：
15
15
-1

实例2:
>>>info = 'abca'
>>> print info.find('a')    # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
0
>>> print info.find('a',1)  # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
3
>>> print info.find('3')    # 查找不到返回-1
-1
>>>

6.字符串查找函数index()
Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

str.index(str, beg=0, end=len(string))
参数
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。
返回值
如果包含子字符串返回开始的索引值，否则抛出异常。

实例:
str1 = "this is string example....wow!!!";
str2 = "exam";
 
print str1.index(str2);
print str1.index(str2, 10);
print str1.index(str2, 40);

15
15
Traceback (most recent call last):
  File "test.py", line 8, in 
  print str1.index(str2, 40);
ValueError: substring not found

shell returned 1


7.字符串判断函数startswith(t)
Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。

str.startswith(str, beg=0,end=len(string));
参数
str -- 检测的字符串。
strbeg -- 可选参数用于设置字符串检测的起始位置。
strend -- 可选参数用于设置字符串检测的结束位置。
返回值
如果检测到字符串则返回True，否则返回False。

实例:
以下实例展示了startswith()函数的使用方法：
str = "this is string example....wow!!!";
print str.startswith( 'this' );
print str.startswith( 'is', 2, 4 );
print str.startswith( 'this', 2, 4 );

以上实例输出结果如下：
True
True
False

8.字符串判断函数endswith(t)
Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。

str.endswith(suffix[, start[, end]])
参数
suffix -- 该参数可以是一个字符串或者是一个元素。
start -- 字符串中的开始位置。
end -- 字符中结束位置。
返回值
如果字符串含有指定的后缀返回True，否则返回False。

实例:
str = "this is string example....wow!!!";
 
suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,20);
 
suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);

以上实例输出结果如下：
True
True
True
False

9.字符串去掉空格函数lstrip()
Python lstrip() 方法用于截掉字符串左边的空格或指定字符。

str.lstrip([chars])
参数
chars --指定截取的字符。
返回值
返回截掉字符串左边的空格或指定字符后生成的新字符串。

实例:
str = "     this is string example....wow!!!     ";
print str.lstrip();
str = "88888888this is string example....wow!!!8888888";
print str.lstrip('8');

以上实例输出结果如下：
this is string example....wow!!!     
this is string example....wow!!!8888888

10.字符串去掉空格函数rstrip()
Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格)

str.rstrip([chars])
参数
chars -- 指定删除的字符（默认为空格）
返回值
返回删除 string 字符串末尾的指定字符后生成的新字符串。

实例:
str = "     this is string example....wow!!!     ";
print str.rstrip();
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('8');

以上实例输出结果如下：

     this is string example....wow!!!
88888888this is string example....wow!!!


11.字符串分离函数split()
Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串

str.split(str="", num=string.count(str))

参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
返回值
返回分割后的字符串列表。

实例1:
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );       # 以空格为分隔符，包含 \n
print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个

以上实例输出结果如下：
['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']


实例2:
txt = "Google#Runoob#Taobao#Facebook"
x = txt.split("#", 1)
print x

以上实例输出结果如下：
['Google', 'Runoob#Taobao#Facebook']