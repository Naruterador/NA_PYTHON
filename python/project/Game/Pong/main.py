import turtle
import os
'''
Windows播放声音方法:
import winsound

winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
'''
class Pong(object):

    def __init__(self,wn):
        self.wn = wn
        #修改窗口标签"Pong Game"
        self.wn.title("Pong Game")
        #修改窗口背景色
        self.wn.bgcolor("black")
        #设置窗口初始化高和宽
        self.wn.setup(width = 800,height = 600)
        self.wn.tracer(0)
        #初始化左边柱子
        self.paddle_a = turtle.Turtle()
        #初始化右边柱子
        self.paddle_b = turtle.Turtle()
        #初始化球
        self.ball = turtle.Turtle()
        #初始化计分牌
        self.board = turtle.Turtle()
        #选手A分数
        self.scoreA = 0
        #选手B分数
        self.scoreB = 0


    def __paddleA(self):
        #设定柱a的移动速度
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        #拉升柱a的长度
        self.paddle_a.shapesize(stretch_wid = 5,stretch_len = 1)
        #隐藏到柱a的坐标线
        self.paddle_a.penup()
        #设定柱a的初始位置
        self.paddle_a.goto(-350,0)


    def __paddleB(self):
        #设定柱b的移动速度
        self.paddle_b.speed(0)
        self.paddle_b.shape("square")
        self.paddle_b.color("white")
        #拉升柱b的长度
        self.paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
        #隐藏到柱b的坐标线
        self.paddle_b.penup()
        #设定柱b的初始位置
        self.paddle_b.goto(350,0)



    def __ball(self):
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        #球的初始位置位(0,0)
        self.ball.goto(0,0)
        #设置球每次移动的横向距离
        self.ball.dx = 2;
        #设置球每次移动的纵向距离
        self.ball.dy = 2;

    def __movepaddleA_up(self):
        y = self.paddle_a.ycor()
        #每次向上移动20
        y = y + 20
        self.paddle_a.sety(y)


    def __movepaddleA_down(self):
        y = self.paddle_a.ycor()
        #每次向下移动20
        y = y - 20
        self.paddle_a.sety(y)


    def __movepaddleB_up(self):
        y = self.paddle_b.ycor()
        #每次向上移动20
        y = y + 20
        self.paddle_b.sety(y)


    def __movepaddleB_down(self):
        y = self.paddle_b.ycor()
        #每次向下移动20
        y = y - 20
        self.paddle_b.sety(y)

    def __moveball(self):
        #设置球每次移动横坐标增加的距离
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        #设置球每次移动纵坐标增加的距离
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    #设置反弹声音
    def __bouncesound(self):
        #afplay用于mac播放声音
        #aplay用于linux播放声音
        #
        os.system("afplay bounce.wav &")
        #添加&表示在后台运行声音

    def __bordercheckBall(self):
        #纵坐标边界检查设置
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
            self.__bouncesound()

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1
            self.__bouncesound()

        #横坐标边界检查设置
        if self.ball.xcor() > 390:
            self.ball.goto(0,0)
            self.ball.dx *= -1
            #横坐标超过390,A得分
            self.scoreA += 1
            #清除当前的计分板，并刷新比分
            self.board.clear()
            self.board.write("Player A: {}  Player B: {}".format(self.scoreA,self.scoreB),align="center",font=("Courier",24,"normal"))

        if self.ball.xcor() < -390:
            self.ball.goto(0,0)
            self.ball.dx *= -1
            #横坐标小于-390,B得分
            self.scoreB += 1
            #清除当前的计分板，并刷新比分
            self.board.clear()
            self.board.write("Player A: {}  Player B: {}".format(self.scoreA,self.scoreB),align="center",font=("Courier",24,"normal"))

        #柱a和球的边界设置
        if self.ball.xcor() > 340 and self.ball.xcor() < 350 and (self.ball.ycor() < self.paddle_b.ycor() + 40) and (self.ball.ycor() > self.paddle_b.ycor() - 40):
            self.ball.setx(340)
            self.ball.dx *= -1
            self.__bouncesound()
        #柱b和球的边界设置
        if self.ball.xcor() < -340 and self.ball.xcor() > -350 and (self.ball.ycor() < self.paddle_a.ycor() + 40) and (self.ball.ycor() > self.paddle_a.ycor() - 40):
            self.ball.setx(-340)
            self.ball.dx *= -1
            self.__bouncesound()

    def __showboard(self):
        self.board.speed(0)
        self.board.color("white")
        self.board.penup()
        #隐藏边框和背景
        self.board.hideturtle()
        self.board.goto(0,260)
        #展示板内容显示
        self.board.write("Player A: 0   Player B: 0",align="center",font=("Courier",24,"normal"))





    def run(self):
        self.__paddleA()
        self.__paddleB()
        self.__ball()
        self.__showboard()
        #显示记分板
        #监听键盘控制输入
        self.wn.listen()
        #柱a向上移动的方法绑定键盘“w”键
        self.wn.onkeypress(self.__movepaddleA_up,"w")
        #柱a向下移动的方法绑定键盘“s”键
        self.wn.onkeypress(self.__movepaddleA_down,"s")
        #柱b向下移动的方法绑定键盘“上”键
        self.wn.onkeypress(self.__movepaddleB_up,"Up")
        #柱b向下移动的方法绑定键盘“下”键
        self.wn.onkeypress(self.__movepaddleB_down,"Down")
        while True:
            self.wn.update()
            #将球每次移动放进事件驱动
            self.__moveball()
            #设置球的边界
            self.__bordercheckBall()


#创建一个窗口
wn = turtle.Screen()
p = Pong(wn)
p.run()
