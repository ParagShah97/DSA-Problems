# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
# Time Complexity: O(log(N))
# Space Complexity: O(1)
from typing import List


class Solution:
    """
    Intuition:
    The main idea is we can apply binary search and when we found the target 
    element rather than stopping we keep the mid value in i and then continue
    For Left case: move right = m-1
    For right case: move left = m+1
    to find the further target element if any in left or the right direction.
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]

    def binary_search(self, nums, target, isLeft):
        l=0
        r=len(nums)-1
        i=-1
        while l<=r:
            m = (l+r)//2
            if target < nums[m]:
                r=m-1        
            if target > nums[m]:
                l=m+1        
            # If found the target ekement then store mid in i and search for
            # further left or right element.
            if target == nums[m]:
                i=m
                if isLeft:
                    r=m-1
                else:
                    l=m+1

        return i