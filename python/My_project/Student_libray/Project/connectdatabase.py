import mysql.connector

class databaseconnect(object):
    
    def __init__(self):
        self.conn = mysql.connector.connect(user='root',password='123456',host='192.168.3.107',port='3306',database='python',use_unicode=True)
        
    def cursor(self):
        c = self.conn.cursor()
        return c
