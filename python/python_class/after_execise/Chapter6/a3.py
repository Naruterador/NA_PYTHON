#编写程序查找某个单词（键盘输入）所出现的行号及该行的内容，并统计该单词在文件共出现多少次。


import codecs


def findword(filename,word):
    s = ''
    newstart = 0
    num = 0
    with codecs.open(filename,"r+",encoding = 'utf - 8') as f:
        s = f.read()
    
    
    while s.find(word,newstart) > 0:
        newstart  = s.find(word,newstart) + 1
        num = num + 1

    print(num)

    
findword("article.txt","钉钉")