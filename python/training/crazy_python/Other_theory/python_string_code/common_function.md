1.len()      获取字符串长度

2.str.strip([chars])
  方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
  实例(Python 2.0+):
	str = "00000003210Runoob01230000000"; 
	print str.strip( '0' );  # 去除首尾字符 0
 
	str2 = "   Runoob      ";   # 去除首尾空格
	print str2.strip();
  
  以上实例输出结果如下：
    3210Runoob0123
    Runoob


3.