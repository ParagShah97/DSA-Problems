# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# Time Complexity: O(N)
# Space Complexity: O(N)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        Intuition: We are using pre-order traversal.
        For each node we check if it None then return None (left node)
        For each node if it either equals to p.val or q.val if yes then return that node.
        Else we call the dfs for left node and then right node.

        At last we check if we find p or q in left/right sub-tree then we will definately
        get non None value, so if both left and right are non None that means current node
        is the lowest common ancestor.
        Else out of left or right is not none that we return.
        Why? - That mean LCS if p and q is one of them.
        """

        def dfs(node, p,q):
            # print("For whih node ", node)
            if not node:
                return None

            if node.val == p.val or node.val == q.val:
                # print("---> ", node.val)
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left and right:
                return node
            else:
                return left or right           
        
        return dfs(root, p, q)