# 433 · Number of Islands      433. 岛屿的个数
# https://www.lintcode.com/problem/433/
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
# Find the number of islands.

from typing import (
    List,
)
from collections import deque

DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]
class Solution:
    '''
    @param grid: a boolean 2D matrix
    @return: an integer
    '''
    def ClearGrid1(self, grid, x, y):                       # from this point (x,y), set all linked point which is 1 to 0
        if(x<0 or x>= len(grid)): return
        if(y<0 or y>= len(grid[0])): return
        if(grid[x][y]==0):return
        grid[x][y] = 0
        self.ClearGrid1(grid, x+1,y)
        self.ClearGrid1(grid, x-1,y)
        self.ClearGrid1(grid, x,y+1)
        self.ClearGrid1(grid, x,y-1)
        return

    def num_islands1(self, grid: List[List[bool]]) -> int:
        # write your code here
        #if (grid.empty() or grid[0].empty()): return 0
        N, M = len(grid),len(grid[0])
        #print(N,M)
        #print(grid)
        cnt=0
        for i in range(N):
            for j in range(M):
                if(grid[i][j]):
                    self.ClearGrid1(grid,i,j)
                    cnt += 1
        return cnt

    def New_Island2(self,grid,x,y,pointVisited):
        pointVisited.add((x,y))
        for delta_x,delta_y in DIRECTIONS:
            x_new = x + delta_x
            y_new = y + delta_y
            if x_new>=0 and x_new<len(grid) and y_new>=0 and y_new<len(grid[0]) and grid[x_new][y_new]==1 and (x_new,y_new) not in pointVisited:
                self.New_Island2(grid,x_new,y_new,pointVisited)

    def num_islands2(self, grid: List[List[bool]]) -> int:
        # write your code here
        #if (grid.empty() or grid[0].empty()): return 0
        if not grid or not grid[0]: return[0]
        N, M = len(grid),len(grid[0])
        #print(N,M)
        #print(grid)
        islandCnt=0
        pointVisited=set()                                       #global: for the whole grid
        for i in range(N):
            for j in range(M):
                #print(i,j,grid[i][j],pointVisited)
                if grid[i][j]==1 and (i,j) not in pointVisited:
                    self.New_Island2(grid,i,j,pointVisited)       #find the 1st point for a new island, then put all points in this island into pointVisited.
                    islandCnt += 1
        return islandCnt

    def New_Island3(self,grid,x,y,pointVisited):
        pointVisited.add((x,y))
        deQ = deque([(x,y)])            #deQ for this island, find all (x,y) in this island, put into visited:
        while deQ: 
            x,y=deQ.popleft()
            for delta_x,delta_y in DIRECTIONS:
                x_new = x + delta_x
                y_new = y + delta_y
                if x_new>=0 and x_new<len(grid) and y_new>=0 and y_new<len(grid[0]) and grid[x_new][y_new]==1 and (x_new,y_new) not in pointVisited:
                    pointVisited.add((x_new,y_new))
                    deQ.append((x_new,y_new))

    def num_islands3(self, grid: List[List[bool]]) -> int:
        # write your code here
        #if (grid.empty() or grid[0].empty()): return 0
        if not grid or not grid[0]: return[0]
        N, M = len(grid),len(grid[0])
        #print(N,M)
        #print(grid)
        islandCnt=0
        pointVisited=set()                                       #global: for the whole grid
        for i in range(N):
            for j in range(M):
                #print(i,j,grid[i][j],pointVisited)
                if grid[i][j]==1 and (i,j) not in pointVisited:
                    self.New_Island3(grid,i,j,pointVisited)       #find the 1st point for a new island, then put all points in this island into pointVisited.
                    islandCnt += 1
        return islandCnt

def main():
    S=Solution()

    Igrid1= [
        [1,1,0,0,0],
        [0,1,0,0,1],
        [0,0,0,1,1],
        [0,0,0,0,0],
        [0,0,0,0,1]
        ]
    print(S.num_islands1(Igrid1))

    Igrid2= [
        [1,1,0,0,0,0,0,0],
        [0,1,0,0,1,0,0,1],
        [0,0,0,1,1,0,1,1],
        [0,0,0,0,0,1,1,1],
        [0,0,0,0,1,0,1,0]
        ]
    print(S.num_islands1(Igrid2))

    Igrid1= [
        [1,1,0,0,0],
        [0,1,0,0,1],
        [0,0,0,1,1],
        [0,0,0,0,0],
        [0,0,0,0,1]
        ]
    print(S.num_islands2(Igrid1))

    Igrid2= [
        [1,1,0,0,0,0,0,0],
        [0,1,0,0,1,0,0,1],
        [0,0,0,1,1,0,1,1],
        [0,0,0,0,0,1,1,1],
        [0,0,0,0,1,0,1,0]
        ]
    print(S.num_islands2(Igrid2))

    Igrid1= [
        [1,1,0,0,0],
        [0,1,0,0,1],
        [0,0,0,1,1],
        [0,0,0,0,0],
        [0,0,0,0,1]
        ]
    print(S.num_islands3(Igrid1))

    Igrid2= [
        [1,1,0,0,0,0,0,0],
        [0,1,0,0,1,0,0,1],
        [0,0,0,1,1,0,1,1],
        [0,0,0,0,0,1,1,1],
        [0,0,0,0,1,0,1,0]
        ]
    print(S.num_islands3(Igrid2))

if __name__ == "__main__":
    main()


# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/tao-mo-ban-bfs-he-dfs-du-ke-yi-jie-jue-by-fuxuemin/
# https://zhuanlan.zhihu.com/p/367780979
# http://chen-tao.github.io/2017/01/27/al-template/
# https://blog.csdn.net/NGUP_LEE/article/details/104760264