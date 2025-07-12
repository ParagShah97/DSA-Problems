# https://leetcode.com/problems/maximum-subarray
# Time complexity: O(N)
# Space complexity: O(1)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Intuition:
        We can use Kadane's algorithm here
        We keep the currSum and maxSum var initialy both assign to 1st elem of array.
        Iterate from 1st element, here we take cur sum + ith element or ith eleme (start 
        new sub array) and assign it to cur sum.
        max sum will be max of cur sum or max sum.
        At last return max Sum.
        """
        curSum = nums[0]
        maxSum = nums[0]

        for i in nums[1:]:
            curSum += i
            curSum = max(curSum, i)
            maxSum = max(curSum, maxSum)
        return maxSum
        
        # # total max will hold overall max 
        # totalMax = nums[0]
        # # curMax will hold the max during the iteration, as soon as it becomes <0 make 
        # # it again 0
        # curMax = 0

        # # Will iterate over the nums:
        # for n in nums:
        #     curMax += n
        #     totalMax = max(curMax, totalMax)
        #     if curMax < 0:
        #         curMax = 0

        # return totalMax