# https://leetcode.com/problems/rotate-image
# Time Compexity: O(N^2)
# Space Compexity: O(1)
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we can rotate the array in 2 steps
        # 1. we first have to take the transpose of the matrix in-place and then
        # 2. We have to reverse all the rows in-place 
        # By this steps we will get the 90 degree rotated matrix.

        # Take the len of matrix in n
        n = len(matrix)
        # Iterate over the right part of the diagonal of the matrix and 
        # swap matrix[i][j] <-> matrix[j][i]
        for i in range(n):
            for j in range(i+1, n):
                temp = matrix[i][j] 
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # Once done with the swapping we have to reverse all the rows.
        for i in range(n):
            matrix[i].reverse()
