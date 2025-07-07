# https://leetcode.com/problems/balanced-binary-tree/
# Time Complexity: O(N)
# Space Complexity O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         '''
#         Intuition: Similar to calculating the height of the tree we can use the same concept, at 
#         any instace of recursion we know that we will get the height of left and right sub tree
#         we just need to calculate the abs difference between left and right height and if the 
#         height is greater tha or equals to 2 then we can make global variable as False.
#         '''
#         ans = True

#         def dfs(node):
#             if not node:
#                 return 0
            
#             left = dfs(node.left)
#             right = dfs(node.right)
#             nonlocal ans
#             if abs(left-right) >=2:
#                 ans= False

#             return 1 + max(left,right)
        
#         dfs(root)
#         return ans

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
    Here I am using a different approach:
    In the recursion dfs, if the node is None then return 0.
    Then first make the left recursion call to the left node.
    {If the left height is -1, when we get -1 that means we already got the 
    scenario where tree is unbalanced}
    Then make the right recursion call to the right node.
    {If the right height is -1, when we get -1 that means we already got the 
    scenario where tree is unbalanced}
    Then main condition: abs(left - right) > 1 return -1
    {This is the first place where we return -1, in case of unbalanced tree.}
    Lastly return 1+max(left,right) heights.

    From the solution we return dfs(root) != -1.
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Base case: height of empty tree is 0

            left_height = dfs(node.left)
            if left_height == -1:
                return -1  # Left subtree is not balanced
            
            right_height = dfs(node.right)
            if right_height == -1:
                return -1  # Right subtree is not balanced

            if abs(left_height - right_height) > 1:
                return -1  # Current node is not balanced

            return max(left_height, right_height) + 1  # Return height if balanced

        return dfs(root) != -1