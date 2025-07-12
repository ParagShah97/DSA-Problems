# https://leetcode.com/problems/validate-binary-search-tree/
# Time Complexty: O(N)
# Space Complexty: O(N)

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition:
        For BST each node except root node should follow condition:
        left sub-node should be smaller than parent but greater than grand-parent node if
        the parent node is the right node grand-parent node.
        Vice-versa for right sub-node.
        Every recursion we check if the node value is greater than the left val
        and smaller than the right value of not then return False.

        Then we can make recursion call 
        For left node.left, left, right as node.val 
        For left node.right, left  as node.val, right

        At last we have to call the dfs with root, left as float('-inf') 
        and right as float('inf').
        """
        
        def dfs(node, left,right):
            if not node:
                return True
            
            if node.val <= left or node.val >= right:
                return False
            # if not left < node.val < right:
            #     return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float('-inf'), float('inf'))
