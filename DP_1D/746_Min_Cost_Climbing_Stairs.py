# https://leetcode.com/problems/min-cost-climbing-stairs/
# Time Complexity: O()
# Space Complexity: O(N)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Intuition:
        Memoization:
        From the start we can either start from 0th or 1st index then we can
        do a dfs.
        If we reach at the index which is  >= n-2 then we can return the cost[i]
        For recursion we can make min(dfs(i+1), dfs(i+2)) and add the current
        cost to it.

        Pure DP:
        Add 0 at the end of the array, then iterate from len(cost)-3 till 0th
        index and at particular index add cost[i] with min(cost[i+1], cost[i+2])
        at last return min(cost[0], cost[1])
        """
        # cache = {}
        # n = len(cost)

        # def dfs(i):
        #     if i >= n-2:
        #         return cost[i]
        #     if i in cache:
        #         return cache[i]

        #     cache[i] = cost[i] + min(dfs(i+1),dfs(i+2))
        #     return cache[i]


        # return min(dfs(0), dfs(1)) 

        # Pure DP solution:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])