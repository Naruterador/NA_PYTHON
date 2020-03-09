#coding = utf - 8

import re

'''
(?<!exp):括号中的子模式必须不出现在匹配内容的左侧，但exp不作为匹配内容的一部分。其实它是(?<=exp)的逆向表达
(?!exp):括号中的的子模式必须不出现在匹配内容的右侧，但exp不作为匹配的一部分。其实它是(?=exp)的逆向表达
(?#comment):注释组。"?#"后的内容是注释，不影响正则表达式本身
示例代码:
'''

print(re.search(r'[a-zA-Z0-9_]{3,}(?#username)@fkit\.org','sun@fkit.org'))
#输出:<_sre.SRE_Match object; span=(0, 12), match='sun@fkit.org'>

#在上面代码中，正则表达式内的(?#username)就是注释，用于对正则表达式的部分内容进行说明。