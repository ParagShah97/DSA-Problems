# https://leetcode.com/problems/summary-ranges/
# Time Complexity: O(N)
# Space Complexity: O(N)
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Intuition:
        Will take a pointer i=0 iterate till len of nums - 1.
        In every iteration keep the track of start value.
        Within the iteration again iterate i to i+1 till nums[i]+1 == nums[i+1]
        condition satisfies, here check i+1 < len(nums) as well.

        Once this inner loop completes, we check
        if start != nums[i] then we append the range from start to ith.
        else: we only append start value.

        At last return final ans. 
        """
        # Better Solution
        if not nums:
            return []
        ans = []    
        i=0
        while i < len(nums):
            start = nums[i]

            while i+1 < len(nums) and nums[i]+1 == nums[i+1]:
                i+=1
            if start != nums[i]:
                ans.append(str(start)+"->"+str(nums[i]))
            else:
                ans.append(str(start))
            
            i+=1
        return ans
        
        # My Solution 
        # if not nums:
        #     return []
        # start = nums[0]
        # ans = []
        # for i in range(len(nums)-1):
        #     if nums[i]+1 != nums[i+1]:
        #         if start != nums[i]:
        #             ans.append(str(start)+"->"+str(nums[i]))
        #         else:
        #             ans.append(str(start))
        #         start=nums[i+1]
        
        # if start != nums[-1]:
        #     ans.append(str(start)+"->"+str(nums[-1]))
        # else:
        #     ans.append(str(start))
        
        # return ans