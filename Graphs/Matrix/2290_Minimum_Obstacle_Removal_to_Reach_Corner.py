# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        """
        Intuition:
        There are 2 almost similar apporaches.
        First: Dijkstra (Greedy which requires minHea | Priority Queue)
        TC (m*n*log(m*n))
        Rather than applying it to the graph(adj) we are applying here on the 
        matrix (grid).

        Here we will keep the minHeap (obsticle, row, col) and visited set (r,c).
        Iterate till minHeap is not empty, now first we check if the current r,c
        is already the end the end cell, then return popped obs.

        Then we prepare the list of all the neigh, then iterate over them:
        Here first we will check if the if the neigh already in the vis or
        nr,nc are in bound (if condition fails we go to next neigh)

        Now, we push the obs+grid(neigh) to the heap and assign neigh as vis.
        Continue to the next cycle.
        ############################################

        Second approach:
        TC O(m*n)
        To reduce the TC by log(m*n), we need to replace the minHeap.
        We can use the deque: where for lower obs we attach from left-end
        and for larger obs we attach from right (rear) end.

        Here we just change the minheap with que, and with in neig loop,
        we check if there is obs (grid[nr][nc]==1) then append(rear) obs+1
        else, attach from front.
        """


        # # First defeine the ROWS AND COLS length
        # ROWS, COLS = len(grid), len(grid[0])

        # minHeap = [(0,0,0)] # (obstacle, row, col)
        # vis = set([(0,0)]) # (rows, cols)

        # while minHeap:
        #     obs, r,c = heapq.heappop(minHeap)

        #     if r == ROWS-1 and c == COLS-1:
        #         return obs
            
        #     neigh = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]

        #     for nr,nc in neigh:
        #         if (nr,nc) in vis or nr < 0 or nc< 0 or nr == ROWS or nc == COLS:
        #             continue
        #         heapq.heappush(minHeap, (obs+grid[nr][nc], nr, nc))
        #         vis.add((nr,nc))
        
        # More optimized code: BFS with deque
        
        # First defeine the ROWS AND COLS length
        ROWS, COLS = len(grid), len(grid[0])

        que = deque([(0,0,0)]) # (obstacle, row, col)
        vis = set([(0,0)]) # (rows, cols)

        while que:
            obs, r,c = que.popleft()

            if r == ROWS-1 and c == COLS-1:
                return obs
            
            neigh = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]

            for nr,nc in neigh:
                if (nr,nc) in vis or nr < 0 or nc< 0 or nr == ROWS or nc == COLS:
                    continue
                # Obsticle
                if grid[nr][nc] == 1:
                    que.append([obs+1,nr,nc])
                else:
                    que.appendleft([obs, nr,nc])
                vis.add((nr,nc))        