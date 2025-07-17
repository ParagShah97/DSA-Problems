# https://leetcode.com/problems/max-area-of-island/
# Time Complexity: O(MxN)
# Space Complexity: O(MxN)
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Intuition:
        Here we will use the idea of dfs, we iterate over the grid as soon as we get 1, we call the 
        i,j index to dfs function, within in the dfs function first we check if the x,y index not valid 
        then return 0, else we will have a counter = 1 and then we make dfs call on all 4 directions
        and whatever counter value return from the call we add up and last return back.

        In the end we update the max area by comparing the current area.
        """
        # Here storing the max area of Island
        maxSize = 0
        # All 4 possible direction
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        # Lenght of grid
        ROWS, COLS = len(grid), len(grid[0])

        # dfs recursive function, to trace the island
        def dfs(r,c):
            # this conditon: will check if the x / y value either already visited or not
            # in the valid range of grid then return 0 (not adding to area)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
            # if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                return 0
            # One way to make as visited
            grid[r][c] = 0
            # initially the size is 0
            size = 1
            for i, j in directions:
                # Adding the size from all the dfs calls in all directions
                size += dfs(r + i, c + j)
            return size
                
        # Iterate over the Rows
        for r in range(ROWS):
            # Iterate over the Cols
            for c in range(COLS):
                # if the island found (1 found) then we call a dfs call and return value is
                # compared if greater than already found maxSize or not.
                if grid[r][c] == 1:
                    maxSize = max(maxSize, dfs(r,c))
        return maxSize