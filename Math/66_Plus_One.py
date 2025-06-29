# https://leetcode.com/problems/plus-one
# Time complexity: O(N)
# Space complexity: O(N)
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Intuition:
        Brute force:
        Create the number from the digit array, add +1 to that num
        then again break the number into digit array, and reverse it and return it.
        """
        # Brute Force
        num = 0
        for i in digits:
            num = num*10 + i
        
        ans = []
        num+=1

        while num > 0:
            d= num % 10
            ans.append(d)
            num = num//10
        
        return ans[::-1]