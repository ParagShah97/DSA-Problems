# https://leetcode.com/problems/same-tree
# Time Complexity: O(N) # N is node from tree have less node in case not equal.
# Space Complexity: O(H)  # H = height of the tree, worst-case O(N)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        # Intuition: Like pre-order traversal we print (do something and then call left & right
        recursion.), same way we recursive call dfs function for ndoe1 and node2 for left & right
        sub-tree. At any instance of the recursion if either of the node is null but other is not
        or if the val of both the node is unequal then we can make the global variable as false.
        '''
        # Approach 1
        # ans = True
        # def dfs(node1, node2):
        #     nonlocal ans
        #     if not node1 and not node2:
        #         return
        #     # Here we are checking for node 1 and node 2
        #     if (not node1 and node2) or (node1 and not node2) or node1.val != node2.val :
        #         ans = False
        #         return

        #     dfs(node1.left, node2.left)
        #     dfs(node1.right, node2.right)
        
        # dfs(p,q)
        # return ans

        # Approach 2:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False