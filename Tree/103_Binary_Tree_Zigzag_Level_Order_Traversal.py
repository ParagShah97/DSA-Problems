# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
# Time Complexity: O(N)
# Space Complexity: O(N)

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Intuition:
        Here we can do level order traversal, take queue to add the root node and 
        till the queue is not empty retrive the node and store value in temp list.
        After each level iteration we check (with the help of counter) if the current
        level need to add normally or reversed.
        At last return the overall list.
        """        
        # queue for level order traversal
        que = deque()
        que.append(root)
        # Counter to check if append array in same order or reverse order.
        counter = 1
        # final answer array
        ans = []

        # Base case: If the current node is None return empty list.
        if not root:
            return []

        # Iterate till the queue is not empty.
        while que:
            # Level order traversal
            q_len = len(que)
            temp = []
            for _ in range(q_len):
                node = que.popleft()
                # If node is not None
                if node:
                    temp.append(node.val)
                    # Add the left and right node to queue.
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            # Add the temp array is same order if counter is odd else reverse and append.
            ans.append(temp if counter % 2 !=0 else temp[::-1])
            counter +=1
        return ans