# https://leetcode.com/problems/n-queens/
# Time Complexity: O(n!)
# Space complexity: O(n^2)

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Intuition:
        The main idea is 2 queen cannot be in same row, col and diagonal.
        For checking the row we only allow a queen in a row, and calling row+1 for recursion.
        For column we keep the col set for each col we check if it alredy exist in the col set 
        that means we already put the queen and continue to check the next column.

        For positive Diagonal we store the (r+c) in the posDiag set, and for any r,c combination
        if r+c in posDiag set then we continue to next col.

        For negative Diagonal we store the (r-c) in the negDiag set, and for any r,c combination
        if r-c in negDiag set then we continue to next col.

        If all the opposite condition bypassed that mean we can put the queen on that location.
        We add the col to col set, r+c to posDiag and r-c to negDiag set.
        Then call backtrack to r+1 row.

        At last we undo all the things we did in backtrack.

        return ans, (when the r == n, we append the board image to the ans array.)
        """
        # cols set will track the column of the queen.
        cols = set()
        # Positive diagonal here we move such that col will increase and row will decrease.
        posDiag = set() # (r+c)
        # Negative diagonal here we move such that row and col both will increase.
        negDiag = set() # (r-c)

        # Initially the board will be of [.] for nxn size.
        board = [["."]*n for i in range(n)]

        ans = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add((r+c))
                negDiag.add((r-c))
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posDiag.remove((r+c))
                negDiag.remove((r-c))
                board[r][c] = "."
        
        backtrack(0)
        return ans