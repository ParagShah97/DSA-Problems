# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Time Complexity: best case O(log(N)) | Worst case skewed BST O(N)
# Space Complexity: best case O(log(N)) | Worst case skewed BST O(N)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Intuition: 
        Iteration approach:
        Iterate till cur is not none.
        Now 2 main condition is there:
        1) if p value and q value both less than curr node value, then
        we move to left sub tree, as both p,q may lies on left side of the
        current node in BST.

        2) if both p & q value greater than curr node value, then we move
        to the right sub tree, as both p,q may lies on right side of the
        current node in BST

        Else we return the current node. {This implis that p smaller and q greater
        than the current node. so we can return the current node.}

        Recursive approach:
        Here in place of chaning the cur to cur.left or cur.right,
        we will make the recursive call with root.left/right.
        The consition will remain the same.
        '''
        # cur = root

        # while cur:
        #     # if p.val > cur.val and q.val > cur.val:
        #     if max(p.val, q.val) < cur.val:
        #         cur=cur.left
        #     # elif p.val < cur.val and q.val < cur.val:
        #     elif min(p.val, q.val) > cur.val:
        #         cur=cur.right
        #     else:
        #         return cur

        if not root or not p or not q:
            return None
        
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return root