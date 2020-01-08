#coding = utf -8

'''
__reversed__():当使用reversed函数翻转对象时调用

'''


class A(object):  
    def __init__(self,num):  
        self.num = num  
      
    def __reversed__(self):  
        ''''' 
        @summary: 当使用reversed函数翻转对象时调用 
        '''  
        ret = []  
        for i in range(self.num):  
            ret.append(self.num - i-1)  
        return ret  
      
if __name__ == "__main__":  
    print (reversed(A(10)))  