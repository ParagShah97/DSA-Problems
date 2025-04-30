# https://leetcode.com/problems/find-peak-element 
# Time Complexity: O(log(N))
# Space Complexity: O(1)
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Intuition:
        If there is only one element just return 0th index.

        For base cases consider if 0th or last index is greatest then we can 
        just return the index by comparing with only 1 neighbor element.

        If not then we can we can apply binary search on the array.
        Steps:
        If cal mid element > both of it's neighbor return mid
        elif cal mid element < mid-1, then move to left (right=mid-1)
        elif cal mid element< mid+1, move to right (left=mid+1)
        """
        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums)-1

        l=0
        r=len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                r = mid-1
            elif nums[mid] < nums[mid+1]:
                l = mid+1 