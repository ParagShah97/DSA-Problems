# https://leetcode.com/problems/squares-of-a-sorted-array/
# Time ComplexityL O(N) Optimal, O(Nlog(N)) Brute force
# Space Complexity: O(N)
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Intuition:
        Brute force approach: TC O(Nlog(N))
        Square all the element in place and then sort the squared array and return it.

        Optimal approach: TC O(N)
        Here we will take 2 pointers, left -> 0th index and right at last index.
        Iterate till left >= right, at each cycle we check the abs value of left &
        right which one greater will be squared and added to the ans array and move
        either left or right which ever is greater.

        At last we need to return the array in the reverse order as all greater elements
        to smaller element square in appending into the array, so the ans array will be 
        in descending order.
        """
        # Let take the 2 pointer start and end
        left = 0
        right = len(nums)-1
        ans = []
        
        while left<=right:
            if abs(nums[left]) <= abs(nums[right]):
                ans.append(nums[right]**2)
                right -=1
            else:
                ans.append(nums[left]**2)
                left+=1
        
        return ans[::-1]