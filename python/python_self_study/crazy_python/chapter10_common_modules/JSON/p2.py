#coding = utf - 8


'''
Python的JSON支持


Python中的json模块提供了将符合格式的JSON字符串恢复成对象的函数，也提供了将对象转换成JSON字符串的方法。

------------------------------------------------------------------------------------
当程序把JSON对象或JSON字符串转换成Python对象时，从JSON类型的转换关系如下:


JSON对象                                      Python类型
 
object(对象)                                   字典(dict)
array(数组)                                    列表(list)
string(字符串)                                  字符串(string)
int(整型)                                      整数(int)
number(real)(实数)                             浮点数(float)
true                                          True
false                                         False
null                                          None

-------------------------------------------------------------------------------------
当程序把Python对象转换成JSON格式字符串时，从Python类型到JSON类型的转换关系如下:

Python类型                                                                                JSON数据类型
字典(dict)                                                                                object(对象)
列表(list)和元组(tuple)                                                                    array(数组)
字符串(string)                                                                            字符串(string)
整形、浮点型、以及整形、浮点型派生的枚举(float,int-& float-derived Enums)                        数值型(number)
True                                                                                     true
False                                                                                    false
None                                                                                     null










'''