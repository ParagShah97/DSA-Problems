# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Time Complexity: O(N)
# Space Complexity: O(N)
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Intuition:
        We can use the idea of monotonic stack. Initailly we have a stack where
        added first element with index 0.
        Iterate over all the elements, inside the iteration we will while loop
        till the top of the element is greater than current element.
        We pop from the stack and then calculate the maxArea
        max Area will be max of current max area, cal curIndex-stack top ele
        index * stack top ele height.

        After that we will add the next element from the height, with
        index either last pop element or current index.

        After that iteration, we again iterate till stack is not empty.
        Here again we will calculate the maxArea.

        At last we will return the max Area.
        """
        # Monotonic stack approach
        stack = [[0, heights[0]]]
        maxArea = 0
        n = len(heights)

        for i in range(1, n):
            updateIndex = i
            while stack and heights[i] < stack[-1][1]:
                temp = stack.pop()
                maxArea = max(maxArea, ((i-temp[0])*temp[1]))
                # stack.append([temp[0], heights[i]])
                updateIndex = temp[0]
            stack.append([updateIndex, heights[i]])
        
        # print(stack)

        while stack:
            tmp = stack.pop()
            maxArea = max(maxArea, ((n-tmp[0])*tmp[1]))
        return maxArea

        # Divivde and conquor
        # if len(heights) ==  1:
        #     return heights[0]
        # if len(heights) ==  2 and (heights[0]==0 or heights[1]==0) :
        #     return max(heights) 
        # def split(arr, l,h):            
        #     area = 0
        #     if l < h:
        #         mid = (l+h)//2
        #         area = max(area, split(arr, l,mid))
        #         area = max(area, split(arr, mid+1,h))
        #         area = max(area, merge(arr, l, mid, h))
        #     return area
        
        # def merge(arr, l,m,r):
        #     ll, rr = m, m+1
        #     minHeight = 0
        #     area = 0

        #     while ll >= l and rr <= r:
        #         if arr[ll] <= arr[rr]:
        #             minHeight = min(arr[ll], arr[rr])
        #             if minHeight == 0:
        #                 area = max(area, arr[ll], arr[rr])
        #             else:
        #                 area = max(area, minHeight * (rr-ll+1))
        #             rr+=1
        #         else:
        #             minHeight = min(arr[ll], arr[rr])
        #             if minHeight == 0:
        #                 area = max(area, arr[ll], arr[rr])
        #             else:
        #                 area = max(area, minHeight * (rr-ll+1))
        #             ll-=1
        #     while ll >= l:
        #         if minHeight <= arr[ll]:
        #             minHeight = min(minHeight, arr[ll])
        #             area = max(area, minHeight * (rr-ll))
        #         ll -= 1
        #     while rr <= r:
        #         if minHeight <= arr[rr]:
        #             minHeight = min(minHeight, arr[rr])
        #             area = max(area, minHeight * (rr-ll))
        #         rr += 1
        #     return area

        # return split(heights, 0, len(heights)-1)