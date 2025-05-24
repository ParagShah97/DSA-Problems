# https://leetcode.com/problems/letter-combinations-of-a-phone-number
# Time Complexity: O(4^n)
# Space Complexity: (N)

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Inuition:
        We case use the simple backtracking approach, we do recursion
        over the digit within the recursion call and and for each digit 
        we iterate over the corresponding character from the dict. 
        """
        ans = []
        # Ditit to character mapper
        numToChar = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9": "wxyz"}
        # Recursion
        def backtrack(idx, cur_str):
            # Base case, when len of cur_str equals to len o digit
            # Add the current string to the ans array
            # Return to next recursion call.
            if len(cur_str) == len(digits):
                ans.append(cur_str)
                return
            
            # Iteration for current chars for corresponding index digit.
            for ch in numToChar[digits[idx]]:
                backtrack(idx+1, cur_str+ch)
            
        if digits:
            backtrack(0, "")
        
        return ans