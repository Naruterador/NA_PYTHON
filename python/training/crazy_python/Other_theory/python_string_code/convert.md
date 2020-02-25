#python3中字符编码转换
> Python3编码转换已经不像python2那样让人崩溃, 但是在使用过程中需要遵循一定规则

各种编码的互相转换, 都要先decode解码为unicode编码, 然后通过unicode再encode编码为想要的编码
s = '我是Python'

####unicode to gb2312<br>
> unicode编码不需要decode()解码，直接encode()编码,如gb2312<br>
> gb2312 = s.encode('gb2312')<br>
> print('gb2312编码:',gb2312) # gb2312编码: b'\xce\xd2\xca\xc7Python'<br>

####gb2312 to utf8
> gb2312编码需要先decode解码成unicode, decode()解码函数中传入的参数为当前字符的编码集,然后再encode编码成utf-8<br>
> utf8 = gb2312.decode('gb2312').encode('utf-8')<br>
> print('utf-8编码:',utf8) # utf-8编码: b'\xe6\x88\x91\xe6\x98\xafPython'<br>

####utf8 to gbk
> 同样的,utf-8编码需要先decode解码为Unicode, 再encode编码换成gbk字符集<br>
gbk = utf8.decode('utf-8').encode('gbk')<br>
print("gbk编码:",gbk) # gbk编码: b'\xce\xd2\xca\xc7Python'<br>

####gbk to uicode
> 当转换成unicode时,直接decode解码就行, 并不需要就行encode()编码<br>
> unicode = gbk.decode('gbk')<br>
> print('unicode编码:', unicode) # unicode编码: 我是Python<br>

####unicode to gb18030
> gb18030=unicode.encode('gb18030')<br>
> print('gb18030编码:', gb18030) # gb18030编码: b'\xce\xd2\xca\xc7Python'<br>
> 从输出结果可以看出gb2312，gbk，gb18030返回的结果都是一样的, 只是3个编码集范围不同.<br>

 

##Python3 中还存在字符字符串与二进制编码转换的问题:
#####二进制 -> 转换 -> 字符串 需要解码 decode
#####字符串 -> 转换 -> 二进制 需要编码 encode

######比如,读取网页的结果:
> response = urllib.request.urlopen( 'http://www.baidu.com' )<br>
> html = response.read() # 此时html就是bytes类型的, 使用需要进行转换<br>

######str to bytes
> print(str.encode(s)) # 字符串转bytes 输出结果:b'\xe6\x88\x91\xe6\x98\xafPython'

######bytes to str
> print(bytes.decode(html) )   # bytes转字符串

