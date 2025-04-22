# Time complexity O(N)
# Space complexity O(1)
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Intuition: Greedy, we will start at the end (len(nums)-2) and traverse
        backward for every step we check current index+current element val is
        greater or equal to goal then we move the goal to the current index.
        This way we can say that we can atleat reach to the goal index from the
        current index and for previous index we only need to reach the updated goal
        as from updated goal index we can reach final index.
        """
        # Initially the goal index is last index
        goal = len(nums)-1
        # Iterate from the last -1 index to 0th index
        for i in range(len(nums)-2,-1,-1):
            # if the current index + value at that index >= current goal
            if i+nums[i] >= goal:
                # Update the goal
                goal = i

        return True if goal == 0 else False