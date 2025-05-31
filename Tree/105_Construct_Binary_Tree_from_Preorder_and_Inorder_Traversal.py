# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# Time Complexity: O(N²)
# Space Complexity: O(N)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Intuition:
        preorder = [3,9,20,15,7] inorder = [9,3,15,20,7]
        We know that the first element in the preorder list will be the root of the tree, we also
        know that the position at which the element present in the inorder list will be a mid.
        That mean all the element from the left to that element in inorder list will be part of
        left sub-tree and all the element to the right will be part of right sub-tree.

        We can divide the pre order from 1 to mid(inclusive) for left tree element 
        and 0 to mid-1(inclusive) for inorder list for left sub-tree, vice-versa for right.
        {i.e: mid+1(inclusive) to end and mid+1(inclusive) to end}  at last return the root.
        '''

        # Base case: if the pre and inorder list is empty.
        if not preorder and not inorder:
            return None

        # Every time the preorder 0th index element will form a root node.
        root = TreeNode(preorder[0])
        # This will help to identify from the inorder list the element from which left elements
        # are the part of left sub-tree and right are the part of right sub-tree. 
        mid = inorder.index(preorder[0])    # As it only consist of unique values.

        # left edge will conect to the return element from the recursionc call for makeing
        # left sub tree.
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # right edge will conect to the return element from the recursionc call for makeing
        # right sub tree.
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root