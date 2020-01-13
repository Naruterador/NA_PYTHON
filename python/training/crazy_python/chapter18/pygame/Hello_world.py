import pygame

#初始化游戏
pygame.init()

#创建一个游戏窗体
screen = pygame.display.set_mode((800,600))

#修改游戏窗口标签栏的标签
pygame.display.set_caption("My First Game")


#游戏启动
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     #如果游戏事件是退出，那就退出游戏
            run = False


pygame.quit()

