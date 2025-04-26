# https://leetcode.com/problems/valid-sudoku
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Intuition: The requirement says that we need to check that same element should not be
        # in row or in column, at the same time same element cannot be in the same 3x3 section.
        # We need 3 data structures 1st to keep the track of if the element is already there in
        # a row.
        # 2nd to keep the track of if the element is already there in a Col.
        # 3rd to check if the number already there in a 3x3 section or not.
        # For 1,2 nd datastructure it's simple mapper[row/col] for the any row or col.
        # Though for 3x3 section we will store a tuple as at any point x,yth cell will be in
        # (x//3,y//3) key. Below describe each tuple is describing 3x3 section.
        # + - - - - - - - - - +
        # | (0,0) (0,1) (0,2) |
        # | (1,0) (1,1) (1,2) |
        # | (2,0) (2,1) (2,2) |
        # + - - - - - - - - - +
        # We have to iterate and if the element in present in any of the data structure at 
        # respective key then return False, else after iteration return True.
        
        # Declare the Data structure
        row, col = len(board), len(board[0])
        rowMapper = {i: set() for i in range(row)}
        colMapper = {i: set() for i in range(col)}
        squareMapper = defaultdict(set)


        # Iterate over the 9x9 matrix
        for i in range(row):
            for j in range(col):
                # If the element is number then only.
                if board[i][j].isnumeric():
                    # Check if the current element in persent ?
                    if (board[i][j] in rowMapper[i]) or (board[i][j] in colMapper[j]) or (board[i][j] in squareMapper[(i//3,j//3)]):
                        # If yes not a valid sudoku
                        return False                        
                    else:
                        # Else add the current element to the respectice DS.
                        rowMapper[i].add(board[i][j])
                        colMapper[j].add(board[i][j])
                        squareMapper[(i//3,j//3)].add(board[i][j])
                        
        return True