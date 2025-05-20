# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Get the lenght of board
        l = len(board)
        # Reverse the board as we numbering starting from
        # bottom left of the matrix
        board.reverse()

        def getIntToCellPosition(cell):
            r = (cell-1) // l
            c = (cell-1) % l
            if r % 2:
                c= l-1-c
            return [r,c]

        # Let start with queue
        q=deque()
        q.append([1, 0]) # Will append the cell number and level
        visited = set()

        while q:
            cell, level = q.popleft()

            for i in range(1,7):
                nextCell = cell+i
                r,c = getIntToCellPosition(nextCell)
                # If the cell don't have -1 then either ladder or snake
                # move the nextcell to the position ladder/snake leading to.
                if board[r][c] != -1:
                    nextCell = board[r][c]
                # If the nextCell not in visited then add the cell to the
                # visited this way we will not visit the cell again.
                if nextCell not in visited:
                    visited.add(nextCell)
                    q.append([nextCell, level+1])
                # if the next cell is the final/dest cell then we can
                # return the level + 1 as total nu. of moves.
                if nextCell ==  l*l:
                    return level+1  # Level is equal to nu. of moves.
        return -1