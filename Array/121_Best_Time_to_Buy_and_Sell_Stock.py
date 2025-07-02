# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Time Complexity: O(N)
# Space Complexity: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Intuition:
        We need to find the max profit, by choosing the correct buy and
        sell day.
        We take buy day at 0th index and sell day start from 1st then
        iterate till last.

        For each cycle we calculate the profit  (sell-buy)
        if profit < 0 then we change the buy day to current day (sell)
        else, we take the max of max profit and current profit.

        At last return the max profit.
        """
        buy_day = 0
        maxProfit = 0

        for sell_day in range(1, len(prices)):
            profit = prices[sell_day] - prices[buy_day]

            if profit < 0:
                buy_day = sell_day
            else:
                maxProfit = max(maxProfit, profit)

        return maxProfit


        