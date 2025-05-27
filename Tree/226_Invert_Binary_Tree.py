# https://leetcode.com/problems/invert-binary-tree
# Time Complexity: O(N)
# Space Complexity: O(H)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Intuition:
        We can use the idea of pre-order traversal, that means as soon we reach the node,
        we swap the left and the right pointer of the node, and then move to left node
        and do the same, and then move to right node and do the same.
        """
        if not root:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root