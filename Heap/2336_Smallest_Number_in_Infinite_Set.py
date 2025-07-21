# https://leetcode.com/problems/smallest-number-in-infinite-set/
# Time Complexity: O(log(N))
# Space Complexity: O(N)

import heapq


class SmallestInfiniteSet:
    """
    Intuition:
    Here there are 2 operations.
    For that will take 3 helper fields 
    1) smallest: it starts from 1 till infinity.
    2) addBackSet, this will store all the element which are added back.
    3) heap {min heap}: this will contain all the elements of addBackSet in min heap form.

    For Pop Smallest:
    There will be 3 condition:
    If there are no elements in the heap then return the smallest element & inc
    by +1.
    Elif: (heap not empty) smallest element < heap top element(min) then return smallest
    field value and inc by +1.
    Else: return the heap top ele, that will be the min element, pop from heap and
    remove from set.

    For add back:
    Here need to check 2 conditions.
    If given number is greater equal to the smallest ele or num is present in set,
    then do nothing and return
    Else: add the number to the set and do heappush the the min heap.

    """

    def __init__(self):
        self.smallest = 1
        # Min heap
        self.heap = []
        self.addBackSet = set()
        

    def popSmallest(self) -> int:
        # If no element in heap
        if not self.heap:
            ret = self.smallest
            self.smallest += 1
            return ret
        # If the smallest eleme < min heap smallest ele,
        # This case when user add back large number
        # Never going to run
        elif self.smallest < self.heap[-1]:
            ret = self.smallest
            self.smallest += 1
            return ret
        # If heap is present and smallest elem > heap smallest,
        # here we will return the min heap top element by poping.
        else:
            ret = heapq.heappop(self.heap)
            self.addBackSet.remove(ret)
            return ret
        

    def addBack(self, num: int) -> None:
        if num >= self.smallest or num in self.addBackSet:
            return
        self.addBackSet.add(num)
        heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)