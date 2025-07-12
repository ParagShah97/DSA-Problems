# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Questions: Is it going to be valid binary tree always ?
        # Is k always going to be valid number ?

        '''
        Intuition:
        Approach 1:
        We know that inorder traversal will give the sorted list in ascending order. So either we
        can make a list: traverse left, store in list, traverse right. And at last we can return
        ans[k-1]

        Approach 2:
        We can use 2 global variable which will store kth smallest node and the k, every time
        in recursion after traversing to the left we decrement the k and of as soon we get k==0
        then we put the current node value into the ans, and in top of all the recursion we will
        check if the ans is -1 none then we return.
        '''
        # Apporach 1
        # ans = []
        
        # def dfs(root, i):           
        #     if not root:
        #         return
          
        #     dfs(root.left, i)
        #     ans.append(root.val)
        #     dfs(root.right, i+1)

        # dfs(root, 0)
        # return ans[k-1]
        
        # Approach 2        
        ans = -1

        def dfs(node):
            nonlocal ans, k
            if ans != -1:
                return
            if not node:
                return
            
            if node.left:
                dfs(node.left)
            k-=1
            if k==0:
                ans=node.val
                return

            if k > 0:
                dfs(node.right)
            
        dfs(root)
        return ans