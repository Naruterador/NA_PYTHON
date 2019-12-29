#coding = utf - 8




'''
某个博物馆最多可以容纳500人同时参观，有一个出入口，该出入口一次仅仅允许一人
通过，参观者的活动描述如下:

参观者动作:
{
	……

	进门(entance)

	……

	参观(visit)

	……

	出门	(exit)
	
	……
}

请添加必要的信号量和P、V[或者wait()、signal]操作，以实现上述过程中
的互斥与同步。要求写出完成的过程，说明信号量的含义并赋初值。

'''



import threading
import sys


class Vmuseum(object):
    
    def __init__(self,enter_num):

        if enter_num > 500:
            sys.exit("The museum just can contian 500 people")
        elif enter_num <= 0:
            sys.exit("You must let at least 1 people get into the museum!")
        else:
            self.enter_num = enter_num
        self.f_enter_num = 0
        self.all_people = enter_num
        self.cond = threading.Condition()
        self.flag = False

    #enterance
    def enterance(self):
        
        self.cond.acquire()
        if self.flag:
            self.cond.wait()
      
        if self.f_enter_num <= self.all_people:
            self.f_enter_num += 1
            print("Now enter visiting member is %d,enter %d person" % (self.f_enter_num,1))
            self.flag = True
            self.cond.notify()

        self.cond.release()




    #visiting
    def visti(self):
        return ("Total visiting people is %d" % (self.enter_num))
   


    #exit
    def exit(self):
        self.cond.acquire()
        if not self.flag:
            self.cond.wait()
        
        if self.enter_num >= 0:
            self.enter_num  -= 1
            print("Now exit visiting member is %d,exit %d person" % (self.enter_num,1))
            self.flag = False
            self.cond.notify()

        self.cond.release()

            
vm = Vmuseum(200)

def enter(times):
    for i in range(times):
        vm.enterance()

def exit(times):
    for i in range(times):
        vm.exit()

threading.Thread(target=enter,args=(200,)).start()
threading.Thread(target=exit,args=(200,)).start()








    
















