# https://leetcode.com/problems/climbing-stairs/
# Time Complexity O(N)
# Space Complexity O(N)
class Solution:
    # def __init__(self):
    #     self.mapper = {}
    
    def climbStairs(self, n: int) -> int:
        # if n <= 1:
        #     return 1
        # if n in self.mapper:
        #     return self.mapper[n]
        # self.mapper[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
        # return self.mapper[n]

        # Approach 2
        """
        Here we can use a DP array of size N+1, from last step and second last step
        we can make only 1 step to reach the last step.
        So Initially we have for n=3 arr will be [0,0,1,1] then we start from
        n-2 index and traverse towards the 0th index.
        At every index we can add the next 2 elements to show what if we took
        1 or 2 step from that index, in that case what will be the overall
        ways from that step to last step.
        """

        # dp = [1] * (n+1)

        # if n <=2:
        #     return n

        # for i in range(n-2, -1, -1):
        #     dp[i] = dp[i+1]+dp[i+2]

        # return dp[0]

        """
        Now rather than, taking the whole array we can have only last 2 steps 
        as the base case and all the remaining steps will be sum of previous
        2 steps.
        """
        first, second = 1,1

        for i in range(n-1):
            temp =first
            first = first+second
            second = temp
        
        return first