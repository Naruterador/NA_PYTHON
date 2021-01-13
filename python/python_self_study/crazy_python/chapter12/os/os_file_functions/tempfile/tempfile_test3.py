#coding = utf - 8






#下面程序示范了如何使用临时文件和临时目录


import tempfile

#通过with语句创建临时目录
with tempfile.TemporaryDirectory() as tmpdirname:
    print('创建临时目录',tmpdirname)





