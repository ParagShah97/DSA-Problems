# https://leetcode.com/problems/number-of-islands
# Time Complexity: O(m*n)+recursion_stack(O(m*n)) = O(m*n)
# Space Complexity: O(m*n)
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Intuition:
        We iterate over the grid row, col wise.
        If we find grid[i][j] == "1" then there is an island, then we 
        can call dfs.
        DFS will check if x, y are in the boundries of grid and cur ele
        is not water if conditon satisfies then we make the land to water
        and search for surrounding diresctions.

        We Keep the counter and every time we found new land we increment 
        the counter. 
        """

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x,y):
            if x<0 or x>=ROWS or y<0 or y>=COLS or grid[x][y] == "0":
                return 
            
            grid[x][y] = "0"

            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        
        islandCount = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islandCount += 1
                    dfs(i,j)
                    
        
        return islandCount