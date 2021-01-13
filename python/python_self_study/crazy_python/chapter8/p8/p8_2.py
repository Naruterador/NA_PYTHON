#coding = utf -8


'''
__len__():当使用len(A)该对象时调用该方法，当没有该方法是会报错，且返回数据不为整数也会报错

'''

class A(object):  
    def __init__(self,num):  
        self.num = num  
        self.start_num = -1  
      
    def __len__(self):  
        ''''' 
        @summary: 当使用len(Test)该对象时调用该方法，当没有该方法是
        会报错，且返回数据不为整数也会报错 
        '''  
        print ("__len__")
        return self.num - self.start_num - 1  
      
if __name__ == "__main__":  
    print (len(A(10)))  