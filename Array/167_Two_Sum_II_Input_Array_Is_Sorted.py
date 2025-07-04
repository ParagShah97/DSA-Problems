# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# Time Complexity: O(O(N))
# Space Complexity: O(1)

from typing import List


class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        """
         Intuition:
            We can use 2 pointers on start and at end.
            We iterate till i< j, & first we calculate sum = num[i]+num[j].
            if sum == target return [i+1,j+1] (as 1-based indexing).
            As the array is sorted moving in right direction greater number,
            moving in left direction smaller number.
            elif sum > target j-=1 (move right ptr to left 1 step)
            elif sum < target i+=1 (move left ptr to right 1 step)
        """
        i = 0
        j = len(num)-1
        while i < j:
            if num[i]+num[j] == target:
                return [i+1,j+1]
            elif num[i]+num[j] < target:
                i += 1
            else:
                j -= 1
        return [-1,-1]