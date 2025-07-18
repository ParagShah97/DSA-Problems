# https://leetcode.com/problems/rotting-oranges/
# Time Complexity: O(M*N)
# Space Complexity: O(M*N)
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Intuition:
        Here we can use the idea of BFS, first we iterate over the grid and add all the 
        rotten oranges indexes to the que, also keep the count of fresh ornages.

        Then we do BFS with that queue and til fresh count > 0.
        Every time we pop element from the queue and check for all 4 directions.
        if x,y grid coordinate out of bound or grid ele != 1, then continue to the next
        direction.
        Else Append it to the queue make it rotten (2), reduce the fresh count. 
        After the iteration just increment the time by 1.

        At last return time if fresh count == 0 else -1.
        """
        ROWS, COLS = len(grid), len(grid[0])
        que=deque()

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    que.append([r,c])
        time = 0

        while que and fresh > 0:
            len_que = len(que)
            for _ in range(len_que):
                x,y = que.popleft()              

                for dx,dy in directions:
                    xx,yy = x+dx, y+dy
                    if xx < 0 or yy < 0 or xx >= ROWS or yy>=COLS or grid[xx][yy] != 1:
                        continue
                    que.append([xx,yy])
                    grid[xx][yy] = 2
                    fresh-=1
   
            time+=1

        return time if fresh == 0 else -1