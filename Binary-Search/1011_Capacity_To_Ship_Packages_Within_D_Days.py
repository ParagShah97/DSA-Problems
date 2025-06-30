# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
# Time Complexity: O(N*log(W))
# Space Complexity: O(1)
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Intuition:
        The problem want to find the min sum weight to put on the ship (one a day)
        It is obvious that min(lower bound to put the weight on any day) will be
        max value from the array. And the upper bound will be the sum of all the 
        weight from array.

        So,we can define lower and upper bound.

        Initially we keep the result (res) as infinite

        It is obvious that the min capacity will be between lower and upper bound
        We can either go with linear or binary, as from lower to upper bound
        is the increasing number sequence.

        We can go with, binary search approach:
        1) mid_capacity will be mid of upper and lower.
        2) We check (with utility func), if mid_cap is enough to put in given days.
        3) If yes then we update the min result and check for more lower cap.
        4) Else, we check for higher that mid_cap.

        Utility Cap function:
        Initially, I take day=1 & sm=0, then iterate over the weights array
        adding ele to sm, as soon the sm values goes above the cap then inc 
        the day by one and change sm to current (new ele from array).
        At last if the day calculated for if smaller than given days then
        return True else False.
        """

        lower,upper = max(weights), sum(weights)
        res = float('inf')

        def capFeasible(capacity):
            day = 1
            sm = 0
            for i in weights:
                sm += i
                if sm > capacity:
                    sm = i
                    day+=1
            return True if day <= days else False


        # Binary Search
        while lower <= upper:
            est_capacity = (lower + upper) // 2

            if capFeasible(est_capacity):
                res = min(res, est_capacity)
                upper = est_capacity-1
            else:
                lower = est_capacity+1

        return res
        