# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Time Compelxity: O(N)
# Space Compelxity: O(N)

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Intuition:
        With global variable, initialte with -1001:
        We can take an ans initially -ve very big number.
        Then we have dfs: Post order traversal.
        If the node is None return 0
        Then we make left and the right recursion call, and get the 
        value left and right sum.

        Here it is optional to take the left or right node value so
        we take max of 0, left/right sum value.
        Before go forward, need to understand there will be 2 values, 
        one will be- till that node what will be the ans if that and sub-nodes
        included.
        two-if the node is part of big path then return only node.val+max(left, right)
        this is to take the max path.

        At last return ans.

        Without global variable.
        rather than returning one we return 2 things every time.
        """
       
        # Without global variable
        if not root.left and not root.right:
            return root.val

        def dfs(node):
            if not node:
                return (0,-1001)
            
            l_s, l_o = dfs(node.left)
            r_s, r_o = dfs(node.right)

            l_s = max(l_s, 0)
            r_s = max(r_s, 0)

            overallSum = node.val + l_s + r_s
            ans = max(overallSum, l_o, r_o)

            return (node.val + max(l_s,r_s), ans)
        
        x,y = dfs(root)
        return y

        # With global variable
        # ans=-1001
        # def dfs(node):
        #     nonlocal ans

        #     if not node:
        #         return 0
            
        #     l_sum = dfs(node.left)
        #     r_sum = dfs(node.right)
            
        #     l_sum = max(l_sum, 0)
        #     r_sum = max(r_sum, 0)
            
        #     # print("-->", node.val, l_sum, r_sum)
        #     overallSum = node.val + l_sum + r_sum
        #     ans = max(ans, overallSum)

        #     return node.val + max(l_sum, r_sum)
        # dfs(root)
        # return ans 
        