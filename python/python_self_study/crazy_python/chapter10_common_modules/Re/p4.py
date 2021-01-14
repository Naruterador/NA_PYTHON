#coding = utf - 8


'''
re.fullmatch(pattern,string,flags=0):该函数要求整个字符串能匹配pattern，如果匹配则返回包含匹配信息的_sre.SRE_Match对象；否则返回None。

re.sub(pattern,repl,string,count=0,flags=0):该函数用于将string字符串中所有匹配pattern的内容换成repl;repl既可是被替换的字符串，也可是一个函数
count参数控制最多替换多少次，如果指定count为0，则表示全部替换。

------------------------------------------------------------------------------------------------------------------------------
Python-字符串前面加r，u，b的理解:

（1）以r或R开头的python中的字符串表示（非转义的）原始字符串

python里面的字符，如果开头处有个r，比如：

(r’^time/plus/\d{1,2}/$’, hours_ahead)

说明字符串r"XXX"中的XXX是普通字符。

有普通字符相比，其他相对特殊的字符，其中可能包含转义字符，即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n"表示换行，"\t"表示Tab等。

而如果是以r开头，那么说明后面的字符，都是普通的字符了，即如果是“\n”那么表示一个反斜杠字符，一个字母n，而不是表示换行了。

以r开头的字符，常用于正则表达式，对应着re模块。

（2）以u或U开头的字符串表示unicode字符串

Unicode是书写国际文本的标准方法。如果你想要用非英语写文本,那么你需要有一个支持Unicode的编辑器。

 

类似地,Python允许你处理Unicode文本——你只需要在字符串前加上前缀u或U。

 

不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。 

一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文, 必须表明所需编码, 否则一旦编码转换就会

出现乱码。 

建议所有编码方式采用utf8

举例：

 

u"This is a Unicode string."

（3）以b或B开头的字符串 b:byte

spython3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes 

python2.x里, b前缀没什么具体意义， 只是为了兼容python3.x的这种写法
'''




import re 

my_date = '2008-08-18'
#将my_date字符串里的中画线替换成斜线
print(re.sub('-','/',my_date))
#将my_date字符串中画线替换成斜线,只替换一次
print(re.sub(r'-','/',my_date,1))

#===============================================

string1 = "abcd1234"
string2 = 'abcd1234k'
pattern = "abcd1234"
print(re.fullmatch(pattern,string1))
print(re.fullmatch(pattern,string2))