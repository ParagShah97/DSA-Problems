# https://leetcode.com/problems/search-insert-position
# Time complexity: O(log(N))
# Space complexity: O(1)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Intuition:
        We can use binary search for this problem, we take l and r pointer and iterate till
        l<=r, we calculate mid.
        if mid ele = target return mid index
        if mid ele < target, move left to mid+1
        if mid ele > target, move right to mid-1
        At last return left.

        Why return left ?
        So in case we don't find the target, so binary search will let to a situaltion where
        l and r pointer crossed each other, in case last comparision if num smaller left
        mmoved to right else move to right which is a tentative position.

        This can also be done with possibleAns variable which will
        nums[mid] < target then possibleAns = mid+1
        else, possibleAns = mid.
        """
        # Not required
        # possibleAns = -1
        l=0
        r=len(nums)-1
        while l<=r:            
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # possibleAns = mid+1
                l = mid+1
            else:
                # possibleAns = mid
                r = mid-1

        return l