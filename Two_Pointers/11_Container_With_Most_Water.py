# https://leetcode.com/problems/container-with-most-water
# Time Complexity: O(N)
# Space Complexity: O(1)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Intuition:
        We can use the 2 pointer approach, left on 0th index and right on last.
        We iterate till we left < right
        At each step we will find the current water level.
        If current level > max level we update the max level
        Then we either move left or right pointer by one step.
        if height of left is less than equals to right then we move left
        else we move right. left(->), right(<-).
        After the interation completed we return the max level.
        """

        maxWater = -1
        left = 0
        right = len(height)-1

        while left < right:
            currentWater = (right-left)*(min(height[left], height[right]))
            maxWater = max(maxWater, currentWater)

            if height[left] <= height[right]:
                left+=1
            else:
                right-=1

        return maxWater