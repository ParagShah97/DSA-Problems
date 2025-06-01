# https://leetcode.com/problems/path-sum
# Time Complexity: O(N)
# Space Complexity: O(N)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Intuition:
        We can do an inorder traversal, first we check if find null node 
        then return False.
        Add the node value to sum.
        If we reach  leaf node and if the target sum equals to current sum
        then return True else return False.

        Lastly, dfs to left with sum OR dfs to right with sum.
        """
        def dfs(node, sum):
            if not node:
                return False
            sum += node.val
            if not node.left and not node.right:
                return targetSum == sum           

            return dfs(node.left, sum) or dfs(node.right, sum)

            
        return dfs(root, 0)