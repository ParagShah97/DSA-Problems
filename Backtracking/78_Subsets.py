# https://leetcode.com/problems/subsets/
# Time Complexity: O(2^N*N)
# Space Complexity: O(N)

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Intuition: Here we can use the basic idea of backtracking.
        For the recursion function we pass the current index and subset array.
        For every recursion call we first append the index's element to the
        subset array and make a recursion call with next index (index+1) &
        subset array. 
        As soon as the index reach the nums lenght then we add the current
        image of the array to the final global ans array.
        At last we return the ans array.
        """
        ans = []
        def dfs(index, subsets):
            if index == len(nums):
                ans.append(subsets[:])
                return
            # First consider the element.
            subsets.append(nums[index])
            # Considered element recursion call.
            dfs(index+1, subsets)

            # Remove the element, or not consider the element.
            subsets.pop()
            # Not Considered element recursion call.
            dfs(index+1, subsets)
        
        dfs(0, [])
        return ans