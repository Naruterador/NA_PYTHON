#coding = utf - 8

import re

'''
(?<=exp):括号中的子模式必须出现在匹配内容的左侧，但exp不作为匹配的一部分
(?=exp):括号中的子模式必须出现在匹配内容的右侧，但exp不作为匹配的一部分

上面两种代码主要用于对匹配内容进行限定，括号中的子模式本身不作为匹配的一部分
例如想要获取HTML代码中<h1>元素的内容。

示例代码:
'''
print(re.search(r'(?<=<h1>).+?(?=</h1>)','help! <h1>fkit.org</h1>! technology'))
#输出:<_sre.SRE_Match object; span=(10, 18), match='fkit.org'>

'''
在上面的正则表达式中，(?<=<h1>)是一个限定组，该组的内容就是<h1>,由于改组用了(?<=exp)声明，因此
在被匹配内容的左侧必须有<h1>;还有一个组是(?=</h1>),该组的内容是</h1>,该组用了(?=exp)声明，因此
要求在被匹配内容的右侧必须出现</h1>
所以，上面的正则表达式会将<h1>和</h1>之间的内容匹配出来。例如:
'''

print(re.search(r'(?<=<h1>).+?(?=</h1>)','help! <h1><div>fkit.org</div></h1>! technology'))
#输出<_sre.SRE_Match object; span=(10, 29), match='<div>fkit.org</div>'>