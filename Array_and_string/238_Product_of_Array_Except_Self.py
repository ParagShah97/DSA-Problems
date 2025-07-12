# https://leetcode.com/problems/product-of-array-except-self/
# Time Complexity O(N)
# Space Complexity O(N)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Intuition: 
        # There can be multiple scenarios:
        # 1. Consider there are no zeros, in that case we can multiple all the elements and then
        #    at any element we just divide by that element to the ovarall multiple and append to
        #    the answer list
        # 2. Consider there is exactly 1 zero then for all the element except 0 will be 0 and at
        #     0 we can have overall multiple of all the ele except 0.
        # 3. Consider there are more than 1 zeros in that call all the values of answer list will
        #    be zeros, we can directly return an array of 0s of lenght equal to input array. 
        #    This is the case as for all the element there will be atleast 1 zero in multiple.
        
        countZeros = 0
        multipleExceptZeros = 1

        for i in nums:
            if i != 0:
                multipleExceptZeros *= i
            else:
                countZeros +=1

        if countZeros > 1:
            return [0]*len(nums)
        ans = []

        for i in nums:
            if i != 0:
                if countZeros == 1:
                    ans.append(0)
                else:
                    ans.append(multipleExceptZeros//i)
            else:
                ans.append(multipleExceptZeros)
        
        return ans