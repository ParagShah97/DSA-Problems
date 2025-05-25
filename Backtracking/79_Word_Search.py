# https://leetcode.com/problems/word-search
# Time Complexity: O(M*N*4^L) 
# Space Complexity: O(L)
from typing import List


class Solution:
    """
    Intuition:
    Here we can use the idea of backtracking.
    Big Idea: We iterate over the matrix and as soon as we get the starting word
    character we pass the x,y 0 (start of the word) to the backtrack function.

    In the backtrack function we fist check if the word_len(or index)==len(word),
    then return True as we able to find all the character from the word.

    Else, we check all the negative condtion like x,y in range of matrix,
    board[x][y] should not equal to #, or board[x][y] != current word character,
    in all this cases we return False.

    Later we make the current board cell as # and then recurse in all 4 directions.
    and or the return bool value with current res.

    Now again we have to revert the board cell back to word, for future comparisions.
    At last return res.   
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def backtrack(x,y,wrd_len):
            if wrd_len == len(word):
                return True
            if x < 0 or x == rows or y < 0 or y ==cols or board[x][y] == "#" or word[wrd_len] != board[x][y]:
                return False
            
            board[x][y] = "#"
            res = False

            res = res or backtrack(x,y+1, wrd_len+1) or backtrack(x,y-1, wrd_len+1) or backtrack(x+1,y, wrd_len+1) or backtrack(x-1,y, wrd_len+1)

            board[x][y] = word[wrd_len]
            return res 
        
        # Iterate over Rows and Column
        # ans=False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i,j, 0):
                        return True
        
        return False