# https://leetcode.com/problems/last-stone-weight/
# Time Complexity: O(N)
# Space Complexity: O(N)

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Intuition:
        We can use max heap, I made all the element as -ve to use normal heapq as max-heap.
        Iterate till len of stones > 1, we take out 2 stones from the heap (largest), take absolute
        difference and then add back to heap if the difference > 0.

        At last if we have stones > 0 then we will return only 1 stone from heap else return 0.
        '''
        l = len(stones)
        if l == 1:
            return stones[0]
        
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        # print(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones,-abs(x-y))

        if stones:
            return -stones[0]
        return 0