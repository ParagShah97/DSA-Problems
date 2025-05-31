# https://leetcode.com/problems/flatten-binary-tree-to-linked-list
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        Intuition:
        As we have to make chnage in place, in the pre-order fashion we
        need to go a opposite approach live reverse post order traversal.
        We will keep a prev pointer (Global) initially None.
        For every recursion we first check if the current node is None, then
        return else call rec to right and then left.
        At last we will make the cur node right points to prev node, and
        make the left of cur node to None and update prev to current node.
        """
        #  I will keep a prev pointer, initially None
        prev = None

        # REcursive function (see intuition)
        def dfs(node):
            nonlocal prev
            if not node:
                return
            
            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None
            prev=node
        
        dfs(root)