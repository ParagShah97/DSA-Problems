# https://leetcode.com/problems/first-missing-positive/
# Time Complexity O(N)
# Space Complexity O(1)
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Intuition:
        We need to make multiple iteration over the array.
        1) In first iteration we will iterate over the array and check if
        number 1 is present or not, and while iterating all the nums[i] value
        goes out of bound (<0 or >len(nums)), we will make it as 1.
        If we do not found 1 in our iteration then we return 1 as ans,
        else we move forward with next iteration.

        2) In next iteration we have different cases.
        For every nums[i] we will take the abosulte value and find index,
        which is nums[i]-1, we make that index element as -nums[i](negative)

        If the index element is already negative that means, already visited
        no need to change anyting.

        3) In the third iteration we check for the first positive value,
        which will illustrate that we unable to reach at that element so 
        our array defenitely don't have that element index+1 value in the
        array.        
        """

        # First Iteration
        foundOne = False
        for i in range(len(nums)):
            if nums[i]==1:
                foundOne=True
            elif nums[i]<=0 or nums[i]>len(nums):
                nums[i] = 1

        if not foundOne:
            return 1
        
        # print("1",nums)
        # Second Iteration
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index] > 0:
                nums[index]=-nums[index]
        
        # print("2",nums)
        # Third Iteration.
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        
        return len(nums)+1