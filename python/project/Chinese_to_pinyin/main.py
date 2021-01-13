from xpinyin import Pinyin
import codecs
import sys


class ChinestoPy(object):

    def __init__(self):
        self.p = Pinyin()
        self.strings = ''

    def __convertfromstring(self, strings):
        self.strings = self.p.get_pinyin(strings, ' ', tone_marks='marks')
        print(self.strings)

    def __convertfromfile(self, filename1,filename2):
        convertcontent = []
        with codecs.open(filename1,'r+',encoding= 'utf - 8') as f:
            content = f.readlines()
            for i in content:
                convertcontent.append(i.strip('\n'))
                convertcontent.append(self.p.get_pinyin(i,' ',tone_marks='marks').strip('\n'))
        
        with codecs.open(filename2,'w+',encoding = 'utf - 8') as f1:
            for i in convertcontent:
                f1.write(i + '\n')


    def __showfilecontent(self, filename):
        with codecs.open(filename, 'r', encoding='utf - 8') as f:
            content = f.readlines()
            for i in content:
                print(i)

    def run(self):
        while True:
            s1 = input('>')
            enterlistmain = s1.split(' ')
            if ('file' in s1) and (2 == len(enterlistmain)):
                try:
                    enterlist1 = s1.split(' ')
                    action = enterlist1[0]
                    filename = enterlist1[1]
                    self.__showfilecontent(filename)
                except Exception as e:
                    print('can not open file %s!' % filename)
                    continue
            elif 'string' in s1:
                try:
                    enterlist2 = s1.split(' ')
                    action = enterlist2[0]
                    strings = enterlist2[1]
                    self.__convertfromstring(strings)
                except Exception as e:
                    print('Wrong input %s' % strings)
                    continue
            elif 'file' in s1 and 3 == len(enterlistmain):
                try:
                    action = enterlistmain[0]
                    filename1 = enterlistmain[1]
                    filename2 = enterlistmain[2]
                    self.__convertfromfile(filename1,filename2)
                except Exception as e:
                    print('Can not find files!')
                    continue
            elif 'exit' == s1:
                sys.exit(0)
            else:
                print('Wrong input!')

c = ChinestoPy()
c.run()
