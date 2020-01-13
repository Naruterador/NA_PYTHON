#coding = utf - 8



'''
有两个磁盘文件text1.txt和text2.txt，各存放一行英文字母，要求把这两个文件中的信息合并
(按字母顺序排列)然后输出到一个新的文件text3.txt中。
'''


import fileinput
import pathlib
import os

p = pathlib.PurePosixPath()
file1 = str(p) + '/text1.txt'
file2 = str(p) + '/text2.txt'



for line in fileinput.input(files=(file1,file2)):
	con = sorted(line)
	for i in con:
		f = open('text3.txt','a+')
		f.write(i)
	f.write(os.linesep)

f.close()