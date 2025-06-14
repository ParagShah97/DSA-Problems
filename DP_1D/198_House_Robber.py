# https://leetcode.com/problems/house-robber/
# Time Complexity O(N)
# Space Complexity O(1) for optimized one.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        Intuition:
        Memiozation:
        We can call dfs(0th index), 
        Now, in dfs function we do a recursion call for i+1 index and
        curent value + i+2 index. I am also using caching to store the
        cache value.

        Pure DP:
        For first 2 index I am taking maximum and storing at 1st index.
        This way we help in calculaion of 3rd index calculation (see
        comment).
        Then we iterate from 2nd index till end, we take max of 
        curr_ele+i-2th, i-1 ele and assign it to current element.
        At last return last element.
        """
        
        # First Memiozation approach:
        # cache = {}

        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in cache:
        #         return cache[i]
            
        #     cache[i] = max(dfs(i+1), nums[i]+dfs(i+2))
        #     return cache[i]
        
        # return dfs(0)

        """ Pure DP """
        # if len(nums) == 1:
        #     return nums[0]

        # # Why?
        # # Consider [2,1,1,2] in this case we are taking 1st and last
        # # element so keeping max of 1st and 2nd element at 1 index
        # # will help in calculate max of first 2 index of 3rd index cal.
        # nums[1] = max(nums[0], nums[1])
        
        # for i in range(2, len(nums)):
        #     nums[i] = max(nums[i-1], nums[i-2]+nums[i])
        
        # return nums[-1]

        """ Most Optimized: """
        rob1, rob2 = 0,0

        # [rob1, rob2, n, n+1, .....]
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2