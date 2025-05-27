# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Time Complexity: O(N)
# Space Complexity: O(H)  # H = height of the tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Intuition:
        We have 2 options either to go left or right, for every call to 
        either of the side the return value need to be added with 1 before 
        returning to the upper level, this will add current level this way 
        are calculating the lenght of each way. 
        To calculate the overall height of the tree we need to to take
        the max of left or right height at current level and pass to 
        upper level.
        '''
        if not root:
            return 0

        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)
        return max(l,r)