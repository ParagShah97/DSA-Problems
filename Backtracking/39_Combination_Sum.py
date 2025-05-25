# https://leetcode.com/problems/combination-sum
# Time Complexity: O(2^t × k)
# Space Complexity: O(k × 2^t)
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Intuition: We need to take elements (can be multiple times to check if it equals to)
        # target, similar logic as finding total subset we will make to recursion call take and
        # not take, but with take call we will pass the same index so in future also we can 
        # retake the same element.

        ans = []
        # Recursive function pass current index, current selected subsets & sum till now.
        def recursion(i, sub, sm):
            # if the sum == target then append the subset to the ans and return
            # we are returning from here as if continues anything adding leads to > sum.
            if sm == target:
                ans.append(sub[:])
                return
            #  Other base cases are if index goes out of bound or if sum already went > target.
            if i >= len(candidates) or sm > target:
                return
            

            # Include case
            # Add the current element to the overall sum
            sm += candidates[i]
            # Append the element to the subset
            sub.append(candidates[i])
            # Make a reccursive call with the same index (as repetation is allowed)
            recursion(i, sub, sm)

            # Not include case
            # Remove the element from the sum
            sm -= candidates[i]
            # pop the element this is for not taken case.
            sub.pop()
            # Make a recursion call for next element.
            recursion(i+1, sub, sm)
        
        recursion(0,[], 0)
        return ans