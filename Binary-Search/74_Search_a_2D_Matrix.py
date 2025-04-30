# https://leetcode.com/problems/search-a-2d-matrix
# Time Complexity (O(log(M*N)))
# Space Compleity O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Intuition:
        First I am going to use binary search vaetially I mean on rows.
        So conditions are like if for a row 0th index < target < last index
        element then for that row again make a binary search horizontally.

        If not then move(l) to upper row if target < 0th index of cur row
        else move(r) to lower row.

        Horizontal biary search, normal binary search for the row which
        is true for 
        if target >= matrix[rowMid][0] and target <= matrix[rowMid][-1]
        """

        rowL, rowR = 0, len(matrix)-1

        def binary_search(i):
            l=0
            r = len(matrix[i])-1

            while l<=r:
                mid =(l+r)//2

                if target == matrix[i][mid]:
                    return True
                elif matrix[i][mid] < target:
                    l=mid+1
                else:
                    r=mid-1
            return False


        while rowL <= rowR:
            rowMid = (rowL + rowR)//2

            if target >= matrix[rowMid][0] and target <= matrix[rowMid][-1]:
                return binary_search(rowMid)
            elif target < matrix[rowMid][0]:
                rowR = rowMid-1
            elif target > matrix[rowMid][-1]:
                rowL = rowMid+1

        return False