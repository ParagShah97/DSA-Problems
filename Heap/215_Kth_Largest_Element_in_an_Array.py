# https://leetcode.com/problems/kth-largest-element-in-an-array
# Time Complexity: O(N*log(N))
# Space Complexity: O(N)
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Intuition: We can do it with heap (min heap of size k), if the size 
        less than k then we push to heap, else we check if the top ele < current ele
        then we replace the top element with the current element.
        At last we return the top element that will the kth largest element.
        """

        heap= []
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            elif heap[0] < i:
                heapq.heapreplace(heap, i)
        return heap[0]