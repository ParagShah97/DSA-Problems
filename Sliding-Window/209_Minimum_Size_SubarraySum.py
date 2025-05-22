# https://leetcode.com/problems/minimum-size-subarray-sum
# Time Complexity: O(2N) = O(N)
# Space Complexity: O(1)
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Intuition:
        We can use the sliding window with 2 pointer to solve this problem.
        We keep the min Len and update the value of it when we find appropiate
        sum value. If sum > target we reduce the sum by removing left ele,
        else we increment the sum by adding right value.
        """

        # Initially the min Len assign to inf
        minLen = float('inf')
        # We can have 2 pointers l and r = 0
        l=r=0
        sm = 0
        # Right pointer will start from 0 to len(nums)
        while r < len(nums):
            sm += nums[r]          
            # When the sum becomes larger than or equal to the target
            # then we update the minLen and decrement the left ele
            # and increment the left index
            while sm >= target and l <= r:
                minLen = min(minLen, r-l+1)
                sm -= nums[l]
                l+=1
            # Increment the right index of next sum.
            r+=1
        # If the minLen never changes then return 0 else minLen.
        if minLen != float('inf'):
            return minLen
        return 0