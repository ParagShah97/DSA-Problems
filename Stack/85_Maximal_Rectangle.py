# https://leetcode.com/problems/maximal-rectangle/
# Time Complexity: O(m*n)
# Space Complexity: O(n)
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Intuition:
        The most important part of the question is to identify that this 
        quesiton can be converted to "84. Largest Rectangle in Histogram"
        Here each row we think as as a base of the histogram, so 3rd row 
        will consider as [3,1,3,2,2].

        Here we start with 0 array and for each row we add the 1's to the
        initial array and if it's 0 then we make it 0 in intital array.

        For each created array we call getMaxArea (where calculate max area),
        return maxArea for that array, out of all max area we takee the max 
        and return the overall max area, this will give the max rectangle.
        """
        
        n = len(matrix[0])
        initialArr = [0]*n
        overAllMax = 0

        # This is same as finding the largest area from the heights array:
        # Refer: 84. Largest Rectangle in Histogram
        def getMaxArea(arr):
            stack = [[0, arr[0]]]
            maxArea = 0

            for i in range(1, n):
                updatedIndex= i
                while stack and arr[i] < stack[-1][1]:
                    temp = stack.pop()
                    maxArea = max(maxArea, ((i-temp[0])*temp[1]))
                    updatedIndex = temp[0]
                stack.append([updatedIndex, arr[i]])
            while stack:
                tmp = stack.pop()
                maxArea = max(maxArea, (n-tmp[0])*tmp[1])
            return maxArea

        for i in range(len(matrix)):
            for j in range(n):
                if int(matrix[i][j]) != 0:
                    initialArr[j] += int(matrix[i][j])
                else:
                    initialArr[j] = 0
            overAllMax = max(overAllMax, getMaxArea(initialArr))

        return overAllMax