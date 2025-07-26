# https://leetcode.com/problems/kth-largest-element-in-a-stream/ 
# Time Complexity: O(N*log(N))
# Space Complexity: O(N)
import heapq
from typing import List


class KthLargest:
    '''
    Intuition: We need to keep the k largest element, so we can keep a heap of size k.
    And as soon we need to add an element whose value is greater than the 0th index element,
    then we can replace the element with the greater value.
    '''

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # If the size of nums if greater then k tnen remove the elements to make the heap size = k.
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    # Add fun time complexity : O(log(k))
    def add(self, val: int) -> int:
        # If the lenght of nums < k then push the incoming values
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        # Else only if the val > 0th index of heap then replace the 0th value with upcoming val.
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)

        return self.nums[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)