import singleton_pattern
import sys

class Student(object):
    def __init__(self):
        self.name = ''
        self.gender = ''
        self.age = 0
        self.identity_id = 0
        #conncect to database
        self.dc = singleton_pattern.databaseC()
        self.c = self.dc.cursor()
    
    
    def __show(self):
        self.c.execute('select * from student_tb')
        result = self.c.fetchall()
        for col in self.c.description:
            print(col[0],end='\t')
        print('\r')

        for row in result:
            for j in range(5):
                print(row[j],end='\t')
            print('\t')
    
    def __insert(self):
        p1 = input('Name:')
        if not self.__checkname(p1):
            return False
        p2 = input('Gender:')
        if not self.__checkgender(p2):
            return False
        p3 = input('Age:')
        if not self.__checkage(p3):
            return False
        p4 = input('Identify_Num:')
        if not self.__checkidd(p4):
            return False
        
        self.c.execute('insert into student_tb values(null,%s,%s,%s,%s)',(self.name,
                        self.age,self.age,self.identity_id))
        
        self.dc.conn.commit()
        


    def __update(self):
        iddnum = input('Input identity_id you wanna modify:')
        if not self.__checkidd(iddnum):
            return False
        if not self.__search(self.identity_id):
            print('Can not find this record in the database!')
            return False
        uname = input('Name:')
        if not self.__checkname(uname):
            return False
        
        ugender = input('Gender:')
        if not self.__checkgender(ugender):
            return False
        
        uage = input('Age:')
        if not self.__checkage(uage):
            return False

        self.c.execute('update student_tb set name=%s where idd=%s',(self.name,self.identity_id))
        self.c.execute('update student_tb set Gender=%s where idd=%s',(self.gender,self.identity_id))
        self.c.execute('update student_tb set age=%s where idd=%s',(self.age,self.identity_id))

        self.dc.conn.commit()


    def __delete(self):
        iddnum = input('Input identity_id you wanna delete:')
        if not self.__checkidd(iddnum):
            return False
        if not self.__search(self.identity_id):
            print('Can not find this record in the database!')
            return False
        
        self.c.execute('delete from student_tb where idd = %s',(self.identity_id,))
        self.dc.conn.commit()
        
        
    def __checkname(self,sname):
        if sname != "" and not sname.isdigit():
            self.name = sname
            return True
        else:
            print('Wrong format of name!')
            return False

    def __checkgender(self,sgender):
        if (sgender == '男' or sgender == '女') and sgender != "":
            self.gender = sgender
            return True
        else:
            print('You can just gender with "男" and "女"!')
            return False
    
    def __checkage(self,sage):
        if int(sage) > 0 and sage != "":
            self.age = sage
            return True
        else:
            print("You are still in your mother's tummy?")
            return False        

    def __checkidd(self,sidd):
        if sidd != "":
            lengthsidd = len(sidd)
            if 18 == lengthsidd:
                self.identity_id = sidd
                return True
            else:
                print('Wrong length of id number,You can just set the length as 18!')
                return False
        else:
            print('Wrong id number format!')
            return False
        


    def __search(self,identity_id):
        self.c.execute('select * from student_tb where idd = %s',(identity_id,))
        result = self.c.fetchone()

        if result:
            return True
        return False
                

    
    def run(self):
        while True:
            s1 = input('>')
            if 'show' == s1:
                self.__show()
            elif 'insert' == s1:
                if not self.__insert():
                    continue
            elif 'update' == s1:
                if not self.__update():
                    continue
            elif 'delete' == s1:
                self.__delete()
            elif 'exit' == s1:
                self.c.close()
                self.dc.conn.close()
                sys.exit(0)
            else:
                print('wrong input!')


s = Student()
s.run()