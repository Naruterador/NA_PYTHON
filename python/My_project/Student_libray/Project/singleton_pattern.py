#单例数据库连接测试代码
import mysql.connector

class databaseC(object):
    
    #定义一个用于记录单例对象的引用变量
    instance = None
    
    def __new__(cls,*args,**kwargs):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        
        return cls.instance

    def __init__(self):
        self.conn = mysql.connector.connect(user='root',password='123456',host='192.168.3.107',database='python',use_unicode=True)
    
    def cursor(self):
        c = self.conn.cursor()
        return c