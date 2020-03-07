'''
ASCII字符范围:
\x00-\x7F(0~127)
'''

from Crypto.Cipher import DES
import struct
import hashlib
import codecs
import sys


class FileEnDe(object):

    def __init__(self):
        self.orkey = ''
        self.data = ''
        self.count = 0
        self.hashkey = ''
        self.head = ''
        self.content = ''
        self.orcontent = ''
        self.encrypted_data = ''
        self.finalen_data = ''

    # 检查key中字符类型是否属于ascii
    def __orkeycheckformat(self, key):
        for i in key:
            if not (ord(i) >= 0 and ord(i) <= 127):
                return False
        return True

    # 检查key中字符长度是否符合要求:
    def __orkeycheck(self, key):
        lengthkey = len(key)
        if self.__orkeycheckformat(key):
            if lengthkey > 8:
                print('Too long key!')
                return False
            elif lengthkey < 8:
                pad = (8 - lengthkey) * chr(0)
                key = key + pad
                key = bytes(key, encoding='utf - 8')
                self.orkey = key
                return True
            else:
                key = bytes(key, encoding='utf - 8')
                self.orkey = key
                return True
        else:
            key = bytes(key, encoding='utf - 8')
            lengthkey = len(key)
            if lengthkey > 8:
                print('Too long key!')
                return False
            elif lengthkey < 8:
                pad = (8 - lengthkey) * chr(0)
                pad = bytes(pad, encoding='utf - 8')
                key = key + pad
                self.orkey = key
                return True
            else:
                self.orkey = key
                return True
    
    #文件内容检查和填充函数
    def __contentcheck(self, filename):
        with codecs.open(filename, 'r+', encoding='utf-8') as f:
            content = f.read()
            self.orcontent = content
        content = bytes(content, encoding='utf-8')
        lengthdata = len(content)
        if (len(content) % 8) != 0:
            # 需要填充的字段数量
            pad = (((lengthdata // 8) + 1) * 8 - lengthdata) * chr(0)
            print(pad)
            pad = bytes(pad, encoding='utf-8')
            content = content + pad
            self.content = content
            self.count = len(self.content)
            return True
        else:
            self.content = content
            self.count = len(self.content)
            return True
 
    
    #加密数据方法
    def __encrypted_data(self,key,filename):
        if self.__orkeycheck(key):
            if self.__contentcheck(filename):
                des = DES.new(self.orkey,DES.MODE_ECB)
                encrypted_data = des.encrypt(self.content)
                self.encrypted_data = encrypted_data
                return True
        return False
                
    #计算文件大小的count方法
    def __headbin(self,count):
        data = struct.pack("@i",count)
        self.head = data
    
    #计算key的哈希值方法
    def __keyhash(self, key):
        md5 = hashlib.md5()
        md5.update(key)
        hashcode = md5.digest()
        self.hashkey = hashcode

    #组合加密后的文件方法
    def __combine(self,key,filename):
        if self.__encrypted_data(key,filename):
            self.__keyhash(self.orkey)
            self.__headbin(self.count)
            
            final_encrypted_data = self.hashkey + self.head + self.encrypted_data
            self.finalen_data = final_encrypted_data

            templist1 = []
            templist2 = []
            tempor1 = []
            tempor2 = []
            for i in range(len(self.finalen_data)):
                if len(templist2) == 16:
                    templist1.append(templist2)
                    templist2 = []
                if len(hex(self.finalen_data[i])[2:]) < 2:
                    templist2.append('0' + hex(self.finalen_data[i])[2:])
                else:
                    templist2.append(hex(self.finalen_data[i])[2:])
            
            #eval() 16进制转10制函数
            tempde1 = []
            tempde2 = []
            for j in templist1:
                for k in j:
                    if eval('0x'+ k) >= 0 and eval('0x' + k) <= 30:
                        tempde2.append('.')
                    elif eval('0x' + k ) == 0:
                        tempde2.append('.')
                    elif eval('0x' + k) >= 0 and eval('0x' + k) <= 127:
                        tempde2.append(chr(eval('0x'+k)))        
                    else:
                        tempde2.append('.')
                tempde1.append(tempde2)
                tempde2 = []

        
            with codecs.open(filename,'w+',encoding='utf-8') as f1:
                for i,j in zip(templist1,tempde1):
                    for k in i:
                        f1.write(k + ' ')
                    f1.write('\t')
                    
                    for x in j:
                        f1.write(x)
                    f1.write('\r')

    #解密加密后文件的方法
    def __decrypt_data(self,key,filename):
        self.__orkeycheck(key)
        self.__keyhash(self.orkey)
        
        if self.hashkey != self.finalen_data[0:16]:
            print('Wrong key can not decrypt the file!')
            return False

        self.__headbin(self.count)
        headlength = len(self.head)
        final_de_data = self.finalen_data[16 + headlength:]
        des = DES.new(self.orkey,DES.MODE_ECB)
        data = des.decrypt(final_de_data)   

        with codecs.open(filename,'w+',encoding='utf-8') as f2:
            f2.write(self.orcontent)
            
    def __show(self, filename):
        with codecs.open(filename, 'r+', encoding='utf-8') as f:
            content = f.readlines()
            for i in content:
                print(i)
        return True
       
    def run(self):
        while True:
            s1 = input('>')
            if 'show' in s1:
                try:
                    enterlist1 = s1.split(' ')
                    show = enterlist1[0]
                    filename = enterlist1[1]
                    self.__show(filename)
                except Exception as e:
                    print('Please type the right filename!')
                    continue
            elif 'encrypt' in s1:
                try:
                    enterlist2 = s1.split(' ')
                    encrypt = enterlist2[0]
                    filename = enterlist2[1]
                    key = enterlist2[2]
                    self.__combine(key,filename)
                except Exception as e:
                    print('Wrong input!')
                    continue
            elif 'decrypt' in s1:
                try:
                    enterlist3 = s1.split(' ')
                    decrypt = enterlist3[0]
                    filename = enterlist3[1]
                    key = enterlist3[2]
                    self.__decrypt_data(key,filename)
                except Exception as e:
                    print('Wrong input!')
                    continue
            elif 'exit' == s1:
                sys.exit(0)
            else:
                print('Wrong input!')


f = FileEnDe()
f.run()

