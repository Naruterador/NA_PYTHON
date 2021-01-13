#!/usr/bin/env python3

'''
代码实现效果：
    输出二维数组2点之间的最短路径条数，从(0,0)到(row,col)


算法说明:
无障碍，右下走，代价相等    动态规划，因为是最短路径，所以每一步只能往右或者往下走，那么到第n步（不在第一行或者第一列）只有两种方式：从上往下来的，或者左往右来的。

所以可设二维数组：dp[m][n]，dp[i][j]即从入口（a[0][0]）走到a[i][j]的最短路径数目，容易推知：
    状态方程：dp[i][j] = dp[i][j-1] + dp[i-1][j]
    边界条件：dp[0][j] 和 dp[i][0]
'''


class Maze(object):

    def __init__(self,row,col):
        self.dpmap = []
        self.row = row
        self.col = col

    def init(self):
        templist = []
        for i in range(self.row ):
            for j in range(self.col):
                templist.append(1)
            self.dpmap.append(templist)
            templist = []



    def shortroadfind(self):
        for i in range(1,self.row):
            for j in range(1,self.col):
                self.dpmap[i][j] = self.dpmap[i][j - 1] + self.dpmap[i - 1][j]

        for i in self.dpmap:
            print(i)

        print(self.dpmap[self.row - 1][self.col - 1])


m = Maze(3,3)
m.init()
m.shortroadfind()

