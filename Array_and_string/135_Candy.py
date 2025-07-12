# https://leetcode.com/problems/candy
# Time Complexity: O(3N)=O(N)
# Space Complexity: O(N)
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Intuition:
        We  need to have 2 passes why- consider cases when array is
        increasing or in decreasing order then we cannot confirm at a
        movement that given number of candies is final in 1 pass.
        example 5,4,3,2-> [2,2,2,1] (1st pass) though it's incorrect.

        We need to keep candies array initailly with 1's.
        Then we have to iterate from left to right 
        and then from right to left (Note that we start at 1 or n-2 index 
        in both the direction.)
        While moving left to right, we check ith from i-1th
        While moving right to left, we check ith from i+1th and
        candy ith <= i+1th for incrementing.
        this way we can confirm the right number of candies for 
        all the childrens.
        """
        n =len(ratings)
        candies = [1]*n

        # Left to right pass check with left element.
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1

        # print("1", candies)

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1]+1
        # print("2", candies)

        return sum(candies)

        