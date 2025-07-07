# https://leetcode.com/problems/diameter-of-binary-tree/
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Intuition: Similar to the problem as calculating the height of the binary tree, we can
        # use the same logic where a fuction will return the height, but at the same time we
        # can store the max diamerter in a global variable.
        
        ans = 0
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal ans
            ans = max(ans, left+right)
            return 1 + max(left,right)
        
        dfs(root)
        return ans