#coding = utf - 8

'''
定义一个正则表达式用于验证国内所有手机号码
'''





'''
#中国电话号码格式:3位网号+4位HLR号+4位的个人代码   长度总和11位

中国移动号段：139　138　137　136　135　134　147　150　151　152　157　158　159　172　178　182　183　184　187　188　198　

中国联通号段：130　131　132　140　145　146　155　156　166　167　185　186　145　175　176　

中国电信号段：133　149　153　177　173　180　181　189　191　199

'''


import re

p = re.compile(r"""((139|138|137|136|135|134|147|150|151|152|157|158|159|172|178|182|183|184|187|188|198|130|131|132|140|
	\-
	145|146|155|156|166|167|185|186|145|175|176|
	\-
	133|149|153|177|173|180|181|189|191|199)(\d{8}))""",re.X)

m = p.findall('asdfsfasfsafasd13815060645138asadfasdfsafsa13861080395adslkjfklas')

print(m)