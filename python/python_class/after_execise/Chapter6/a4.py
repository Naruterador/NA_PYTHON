'''
设一个文本文件marks.txt中存储了学生的姓名及成绩如下：
张三  96
李四  95
……
每行为学生姓名与成绩，编写一个程序读取这些学生的姓名与成绩并按成绩的从高到低的顺序输出到另外一个文件sorted.txt中。
'''


import codecs
import operator

temp = []
dict1 = {}
dict2 = {}
#打开marks.txt并将读取文件内容压入列表
with codecs.open("marks.txt","r+",encoding = "utf - 8") as f:
    for i in f.readlines():
       t = i.strip("\n").split('  ')
       temp.append(t)

#将列表容放入字典
for i in range(len(temp)):
    temp[i][1] = int(temp[i][1])
    dict1[temp[i][0]] = temp[i][1]
    dict2.update(dict1)

#字典根据值排序
sorted_dict = sorted(dict2.items(),key = operator.itemgetter(1))

with codecs.open("sorted.txt","w+",encoding = "utf-8") as f1:
    for i in sorted_dict:
        f1.write(str(i[0]) +"  "+ str(i[1]) + '\n')