# https://leetcode.com/problems/sum-root-to-leaf-numbers
# Time Complexity: O(N)
# Space Complexity: O(H + L × H) → O(N²) worst case

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
    We can use preorder traversal pattern here!.
    Call the dfs function with root node and empty list.
    First we push the current node value to the current list,
    then we check if the current node is leaf node or not, if
    the current node is a leaf node then we will append all the
    digits from the current list to ans list (as a string number).

    Later we traverse to the left and then right node of the tree.
    Then at last we pop the current node element from the current list,
    pop operation.

    Finally, we sum all the number (convt from str to number) and
    return the addition.
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = []

        def dfs(node, cur_lst):
            if not node:
                return
            
            cur_lst.append(str(node.val))
            if not node.left and not node.right:
                # print("what list ",cur_lst)
                ans.append("".join(cur_lst))
                cur_lst.pop()
                return
            
            dfs(node.left, cur_lst)
            dfs(node.right, cur_lst)
            cur_lst.pop()
        dfs(root, [])
        sm =0
        for val in ans:
            sm+=int(val)
        return sm