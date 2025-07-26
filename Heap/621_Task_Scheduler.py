# https://leetcode.com/problems/task-scheduler/
# Time Complexity: O(log(n)+O(N)) = O(N), heap and iteration.
# Space Complexity: O(N)

from collections import deque
import heapq
from typing import Counter, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Intuition:
        The main idea is count the freq of all the task and put the freq to the heap.
        Iterate till the heap (max heap) or que is not empty. Every time 
        if heap non-empty take an element out reduce the units and add units and
        time when that task can be exe again to que if units not 0. As we are 
        keeping the time (inc by 1 every iteration) we need to check if que top ele
        reach the time then we can pop out again add it to heap. 
        """
        cnt = Counter(tasks)
        heap = []
        for _,v in cnt.items():
            heapq.heappush(heap, -v)
        print(heap)
        time = 0
        que = deque()

        while heap or que:
            time += 1
            '''
            Below if condition will check if the heap is not empty then,
            pop the max element (max heap), +1 to it (python max heap is -ve min heap).
            If the units == then we no need to add the units along with time to que.
            '''
            if heap:
                units = heapq.heappop(heap)
                units +=1
                if units != 0:
                    que.append((units, time+n))
                # print("111 ", heap, que, time)
            '''
            Below if condition will check if the top element in the que with time is reached
            if yes then pop the unit and add it again to heap.
            '''
            if que and que[0][1] == time:
                pop_unit, _ = que.popleft()
                heapq.heappush(heap, pop_unit)
                # print("222 ", heap, que, time)
        
        return time