# https://leetcode.com/problems/symmetric-tree
# Time Complexity: O(N)
# Space Complexity: O(N)
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        """
        Intuition:
        We can do level order traversal here!
        For each level we will keep an cur_array and add all the non None node.val
        and for None val we add the special symbol, at the end of each level,
        we call a check function to check the element in right palindrom order
        or not. If not we return False else we will 
        """
        # Base case when only root node is present.
        if not root.left and not root.right:
            return True

        # Mrthod to check if an array is palidorme or not.
        def check(nums):
            l = 0
            r = len(nums)-1

            while l < r:
                if nums[l] != nums[r]:
                    return False
                l+=1
                r-=1
            
            return True
        
        # Level Order search 
        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            cur_arr = []

            while q_len > 0:
                curNode = q.popleft()
                q_len -= 1

                # If the current node is not None then we add the 
                # cur val to the cur_arr else we add special symbol "#"
                if curNode:
                    cur_arr.append(curNode.val)
                    q.append(curNode.left)
                    q.append(curNode.right)
                else:
                    cur_arr.append('#')
            # Check for current level array.
            if not check(cur_arr):
                return False
        # Lastely return True.
        return True