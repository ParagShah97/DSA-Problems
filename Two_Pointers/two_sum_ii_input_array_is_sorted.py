# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# Time Complexity O(N)
# Space Complexity O(1)
from typing import List


class Solution:
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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1    

        while i < j:
            s = numbers[i]+numbers[j]
            # sum == target
            if s == target:
                return [i+1, j+1]
            elif s > target:
                j-= 1
            elif s < target:
                i+=1

        return [-1,-1]