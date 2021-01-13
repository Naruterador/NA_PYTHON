# 汉字转拼音
<pre>
    1. 程序执行后显示"PY>"的提示符号，执行的命令是"string 句子"的功能是把一个中文句子转为拼音，例如：

        PY>string 很神奇

        hěn shén qí

        PY>

        
      > 执行命令"file 文件名称"的功能是显示文件的内容，例如：

        PY>file books.txt

        汉字转Pinyin

        深圳信息职业技术学院

        PY>
        

      > 执行命令"file 源文件 目标文件"的功能是把源文件的每条中文句子转为拼音，例如：

        PY>file books.txt bookspy.txt

        汉字转Pinyin

        hàn zì zhuǎn Pinyin

        深圳信息职业技术学院

        shēn zhèn xìn xī zhí yè jì shù xué yuàn
    2、安装拼音库

        > 中文转拼音的核心是xpinyin库，首先安装这个库：

            pip install xpinyin

    3、获取拼音库的使用方法

        >>> import xpinyin

        >>> help(xpinyin.Pinyin)

        Help on class Pinyin in module xpinyin:

        

        class Pinyin(builtins.object)

        translate chinese hanzi to pinyin by python, inspired by flyerhzm’s

        `chinese\_pinyin`_ gem

        

        usage

        -----

        ::

        

        >>> from xpinyin import Pinyin
 |      >>> p = Pinyin()
 |      >>> # default splitter is `-`
 |      >>> p.get_pinyin(u"上海")
 |      'shang-hai'
 |      >>> # show tone marks
 |      >>> p.get_pinyin(u"上海", tone_marks='marks')
 |      'shàng-hǎi'
 |      >>> p.get_pinyin(u"上海", tone_marks='numbers')
 |      >>> 'shang4-hai3'
 |      >>> # remove splitter
 |      >>> p.get_pinyin(u"上海", '')
 |      'shanghai'
 |      >>> # set splitter as whitespace
 |      >>> p.get_pinyin(u"上海", ' ')
 |      'shang hai'
 |      >>> p.get_initial(u"上")
 |      'S'
 |      >>> p.get_initials(u"上海")
 |      'S-H'
 |      >>> p.get_initials(u"上海", u'')
 |      'SH'
 |      >>> p.get_initials(u"上海", u' ')
 |      'S H'
 |  
 |  请输入utf8编码汉字
 |  .. _chinese\_pinyin: https://github.com/flyerhzm/chinese_pinyin
 |  
 |  Methods defined here:
 |  
 |  __init__(self, data_path='/usr/lib/python3.8/site-packages/xpinyin/Mandarin.dat')
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  get_initial(self, char='你')
 |  
 |  get_initials(self, chars='你好', splitter='-')
 |  
 |  get_pinyin(self, chars='你好', splitter='-', tone_marks=None, convert='lower')
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  convert_pinyin(word, convert)
 |  
 |  decode_pinyin(s)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  data_path = '/usr/lib/python3.8/site-packages/xpinyin/Mandarin.dat'

 
</pre>