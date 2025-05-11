# https://leetcode.com/problems/contains-duplicate-ii
# Time Complexity: O(N)
# Space Complexity: O(N)
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Intuition:
        We can have a dict to keep the latest index of the element found
        in the nums array.
        We will iterate over the nums array and check if the element already
        in the dict and current index - dict[sameval]'s index <= k then
        return True. Every cycle we update/add the index to the dict.

        At last return false.
        """

        countDic = {}

        for i in range(len(nums)):
            if nums[i] in countDic and i-countDic[nums[i]] <= k:
                    return True                
            countDic[nums[i]] = i
        
        return False