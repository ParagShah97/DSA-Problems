# https://leetcode.com/problems/find-the-duplicate-number/
# Time Complexity: O(N)
# Space Complexity: O(1)
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Intuition:
        Here we need to consider the problem as linked list problem, as we know that
        there are n+1 integers in list within range 1 to n so 1 number will be repeating
        also, all the value at any index will points at the another index witin in the 
        array (example at index 0-> 3 that means 0 points to 3rd index element and so on).

        We can use slow and fast pointer, to detect the start of the loop witin the LL.
        The fact is start point of the LL will always a repeating number.
        '''
        slow = fast =0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 =0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow