# https://leetcode.com/problems/search-in-rotated-sorted-array
# Time Complexity: O(log(N))
# Space Complexity: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Intuition:
        We can use binary search here!
        First we can calculate mid, if mid ele = target return index.
        If not we first check if the left array is sorted or not by
        
        1. IF:
        (nums[low]<=nums[mid])
        If yes then we check if 
        target > nums[low] and target <= nums[mid] (then high=mid-1)
        else: low=mid+1

        2. ELSE:
        then check (nums[mid] < target and target <= nums[right])
        then low = mid+1
        else: high = mid-1 {Even though the right part sorted by target in
        left part}
        """
        l=0
        r=len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            
            # Check if the left sub array is sorted ?
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid-1
                else:
                    l=mid+1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l=mid+1
                else:
                    r=mid-1

        return -1