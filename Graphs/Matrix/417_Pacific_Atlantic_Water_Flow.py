# https://leetcode.com/problems/pacific-atlantic-water-flow
# Time Complexity: O(M∗N)
# Space Complexity: O(M∗N)
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Intuition:
        We will consider all 4 corners rows and cols. 
        For top row we will make a dfs call for each elements for visit set pacific.
        For bottom row we make a dfs call for each elements for visit set atlantic.
        Similarly for left col -> pacific
        Similarly for right col -> Atlantic
        The main idea is we make dfs call for all the 4 direction where we check if 
        the cell already in (pac or atl) in the height < prvious height (we are going
        in the opposite direction so the cell we are going inward should have greater 
        height that the current). (Check comment in DFS)
        If all this condition is not true then we can add the cell to visit set.

        At last we can check the overlapping cells from pac and atl sets and return a
        list of them.
        '''

        # Let have 2 sets pacific and atlantic they context cell indexes.
        pacific_set = set()
        atlantic_set = set()

        # Rows and Cols
        ROWS, COLS = len(heights), len(heights[0])

        # Possible direction
        directions = [[1,0], [-1,0], [0,1], [0, -1]]

        # dfs function for iteration from corners to inner cells
        def dfs(x,y, cur_set, prevH):
            if x<0 or x>=ROWS or y<0 or y>=COLS or (x,y) in cur_set or heights[x][y] < prevH:
                return
            cur_set.add((x,y))
            for i, j in directions:
                row,col = x+i,y+j
                dfs(row, col, cur_set, heights[x][y])

        # Iterate
        for i in range(COLS):
            dfs(0, i, pacific_set, heights[0][i]) 
            dfs(ROWS-1, i, atlantic_set, heights[ROWS-1][i])
        
        for i in range(ROWS):
            dfs(i, 0, pacific_set, heights[i][0]) 
            dfs(i, COLS-1, atlantic_set, heights[i][COLS-1])

        # Check if cell indexes present in both pacific and atlantic sets.
        ans = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacific_set and (i,j) in atlantic_set:
                    ans.append([i,j])
        return ans                     