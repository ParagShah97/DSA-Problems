# https://leetcode.com/problems/house-robber-ii/
# Time Complexity: O(N)
# Space Complexity: O(1)
from typing import List


class Solution:
    """
    Intuition:
    Here the util function is same as the house robber.
    We will call the util function to find the maximum of 0th index
    or util call for 1st index to last index element, or 0th to n-1
    element.
    """

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.util(nums[1:]), self.util(nums[:-1]))
        
    
    def util(self, nums):
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
