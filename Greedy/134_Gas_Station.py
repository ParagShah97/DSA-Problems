# https://leetcode.com/problems/gas-station
# Time Complexity O(N)
# Space Complexity O(1)
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        """
        Intuition:
        If the total sum of gas < sum of costs then not possible return -1.
        Else, we will iterate over index of gas and cost.
        we calculate total += gas[i]-cost[i]
        this way for each index we check if the difference of gas and cost.
        if the difference is less than zero then we cannot take any index before
        that index. We again make the total 0 and assign ans to i+1 and continue
        to check further.
        """

        # If gas < cost array return -1
        if sum(gas) < sum(cost):
            return -1

        total = 0
        ans=0

        for i in range(len(gas)):
            # sum total till current index.
             total += gas[i]-cost[i]
            #  if total till current index < 0
             if total < 0:
                # Make total = 0 (we have to restart from current index)
                total = 0
                # ans cannot be any previous element so best choice 
                # is upcoming next element.
                ans = i+1
        return ans