# https://leetcode.com/problems/subtree-of-another-tree/
# Time Complexity: O(N)
# Space Complexity: O(N)

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Intuition:
    Here I use the idea of similar question checking equal tree.
    Starting from the root node of both the tree, if main tree node val not equals
    to other tree node then we move in the main tree in pre-order fashion.
    As soon we get the node value equal call the check if same tree function, this
    function recursively check if both the tree are same or not and return  T/F 
    accordingly.
    """
    # This funtion will make the recursion call to check from the current node (main tree)
    # and root node of other tree, are they equal or not.
    def checksubTree(self,p,q):
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return self.checksubTree(p.left, q.left) and self.checksubTree(p.right, q.right)
        else:
            return False
    # This is the main function
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case if the subRoot is None
        # Then obviously None can be sub-tree of main tree, so True
        if not subRoot:
            return True
        # Base case: if the root is None but subTree is not
        # then not matching return False.
        if not root and subRoot:
            return False
        # If root and subroot not None and both have equal value then
        # Call the checkSubTree function.
        if root and subRoot and root.val == subRoot.val and self.checksubTree(root,subRoot):
            return True
        # If the current root node value not equal then move the root in pre-order fashion.
        # keeping th subRoot same.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)