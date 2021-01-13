#coding = utf - 8

'''
join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join(seq);

以上实例输出结果如下：
a-b-c
'''

import os

#待遍历文件的路经
path = '/etc'

#输出目录下所有文件
dirs = os.listdir(path)

for file in dirs:
	#os.path.join(path,file)用于将目录和文件名合成一个路径
	print(os.path.join(path,file))
