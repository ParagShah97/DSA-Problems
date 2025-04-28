# https://leetcode.com/problems/two-sum
# Time Complexity O(N)
# Space Complexity O(N)
from typing import List


class Solution:
    """
    Intuition:
    I am keeping a hashtable, to keep the already visted number with index.
    Every time I check if target - current number if exists in hash map
    then just return hashMap[target-curNum], curIndex.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashVals = {}
        for i in range(len(nums)):
            if target - nums[i] in hashVals:
                return [hashVals[target -nums[i]], i]
            hashVals[nums[i]] = i
        return [-1,-1]