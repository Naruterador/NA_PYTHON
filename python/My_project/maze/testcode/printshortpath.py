#!/usr/bin/env python3


'''
代码功能:
    打印出2维数组两点之间的所有最短路径.

实现帮助:
深度优先算法
'''


import random

class NodeClass(object):
    def __init__(self,i,j,v):
        self.i = i
        self.j = j
        self.v = v


class MazeClass:

    def __init__(self,m,n):
        self.m = m
        self.n = n
        self.maze = []

    def init(self):
        templist = []
        for i in range(self.m):
            for j in range(self.n):
                templist.append(0)
            self.maze.append(templist)
            templist = []

    def showlist(self):
        self.init()
        for i in self.maze:
            print(i)



    def DFSseek(self):
        print("**********DFSseek_Algorithm*************")
        stack = []
        stack.append(NodeClass(0,0,0))
        top = 0
        count = 0

        while top >=0:
            node = stack[top]
            v = node.v
            node.v = v + 1

            if v == 0:
                i = node.i
                j = node.j - 1
            if v == 1:
                i = node.i
                j = node.j + 1
            if v == 2:
                i = node.i - 1
                j = node.j
            if v == 3:
                i = node.i + 1
                j = node.j

            if v < 4:
                if i >= 0 and j >=0 and i < self.m and j < self.n:
                    flag = False
                    for k in range(top + 1):
                        if stack[k].i == i and stack[k].j == j:
                            flag = True
                            break
                    if self.maze[i][j] == 0 and not flag:
                        node = NodeClass(i,j,0)
                        stack.append(node)
                        top = top + 1
                        if i == self.m - 1 and j == self.n - 1:
                            count = count + 1
                            print("Path %-4d" % count,end = ":")

                            for k in range(top + 1):
                                print("--(%d,%d)" % (stack[k].i,stack[k].j),end = "")
                            print('\r')
                            stack.pop()
                            top -= 1
            else:
                stack.pop()
                top -= 1

        if count == 0:
            print('Cant find any way out from this maze!')
        return count


m = MazeClass(3,3)
m.showlist()
m.DFSseek()
