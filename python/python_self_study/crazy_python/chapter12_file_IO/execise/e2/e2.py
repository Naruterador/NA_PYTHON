#coding = utf - 8



'''
提示用户不断输入多行内容，程序自动将内容保存到my.txt中，知道用户输入exit为为止。
'''

import sys
import os

while True:
	userinput = input('Please input the Content:')
	if userinput == 'exit' or userinput == 'Exit':
		f.close()
		sys.exit(0)
	else:
		f = open('my.txt','a+')
		f.writelines(userinput + os.linesep)

