# https://leetcode.com/problems/spiral-matrix
# Time Complexity: O(N*M)
# Space Complexity O(N*M)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Store rows and cols len
        rows, cols = len(matrix), len(matrix[0])
        # Directions (->, v, <-, ^)
        direct = [[0,1], [1,0], [0,-1], [-1,0]]
        # Starting indexes
        i=j=0
        # Currect direction of movement
        curDir = 0
        ans = []

        # Initially I put the 0,0 already in ans list
        ans.append(matrix[i][j])
        matrix[i][j] = '#'
        # Iterate till ans list len is less than total number of elements
        while len(ans) < (rows*cols):
            # Get the updated coordinate.
            i += direct[curDir][0]
            j += direct[curDir][1]

            # Check if i and j in range and mat elem != # (special char to check
            # if the ele already visited or not.)
            if i >= 0 and i<rows and j >= 0 and j<cols and matrix[i][j] != '#':
                # If not visited then add to list and mark as visited.
                ans.append(matrix[i][j])
                matrix[i][j] = '#'
            else:
                # If out of range or reach to already visted element then
                # Reverse the step and change the direction to next direction.
                i -= direct[curDir][0]
                j -= direct[curDir][1]
                curDir = (curDir+1)%4
        return ans   