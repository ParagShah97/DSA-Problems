# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
# Time Complexity: O(N²)
# Space Complexity: O(N)

# TODO: Need to Optimize it!

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Intuition:
        We know that the last ele of the postorder array will be the 
        root node the tree/sub-tree. Also we know that the index at which
        the root node is present in the inorder array will be in mid and
        the left sub-array and right sub-array will be left and right subtrees
        respectively.

        So, initially we will be having a base case when both the arrays
        are empty return None.
        Then we create a node for root node, (last elem of postorder),
        then find the index if that elem in inorder array. 
        Then use the index to call left sub-tree and attach to root.left
        Then use the index to call right sub-tree and attach to root.right.
        """
        if not inorder and not postorder:
            return None 
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)

        root.left = self.buildTree(inorder[0:mid], postorder[0:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid: -1])

        return root