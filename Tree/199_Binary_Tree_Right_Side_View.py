# https://leetcode.com/problems/binary-tree-right-side-view/
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Intuition:
        Here I am using the idea of BFS-level order traversal.
        {Here I not describing about the Level order traversal}
        Then we can take last variable which keep the val of node val
        removing from the queue, (all the val, getting updated).
        In every cycle if last var is not None update the value to the
        final ans. At last return final ans.
        """
        if not root:
            return []
        
        que = deque()
        que.append(root)
        ans = []

        while que:
            len_q = len(que)
            # temp = []
            last = None
            for _ in range(len_q):
                node = que.popleft()

                if node:
                    last = node.val

                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            # if temp:
            #     ans.append(temp[-1])
            if last is not None:
                ans.append(last)
        
        return ans