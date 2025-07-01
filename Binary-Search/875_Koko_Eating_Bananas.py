# https://leetcode.com/problems/koko-eating-bananas/
# Time Complexity: O(n*log(w))
# Space Complexity: O(1)
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Intuition:
        We are given with piles and total hrs, we need to find speed (k) at which
        koko can eat such that, hrs took by koko will be less than equal to give h.

        So we say that we lower and upper bound speed, lower=1 and upper=max val from
        pile. We need to minimize the speed (k).

        We take res as very big number.

        We can apply linear or binary search from lower to upper bound.
        Optimal go for binary search:
        While lower <= upper bound (speed)
        1) Find mid speed and then check (utility fun) speed works ?
        2) If Yes, then update the res for min of res, calculated mid speed
            and update upper bound speed to mid_spd-1 
        3) If No then update lower bound speed to mid_spd+1
        Return final res.

        Utility function:
        It will take the current speed (mid_speed)
        Here we keep hrs = 0
        Iterate over the piles and cal ceil of (float(i)/spd) and
        add it to the hrs.
        At last we check if the hrs <= given h then return True
        else False.
        """
        
        lower, upper = 1, max(piles)
        res = float('inf')

        def checkEatingSpeed(spd):
            hrs = 0
            for i in piles:
                hrs += math.ceil(float(i)/spd)
            return True if hrs <= h else False


        while lower <= upper:
            bananaPerHr = (lower+upper)//2

            if checkEatingSpeed(bananaPerHr):
                res= min(res, bananaPerHr)
                upper = bananaPerHr-1
            else:
                lower = bananaPerHr+1
        
        return res