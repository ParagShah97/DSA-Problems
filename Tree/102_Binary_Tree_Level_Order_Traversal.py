# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Time Complexity: O(N), here N is number of Node.
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Intuition:
        Level order traversal we can think of BFS. As we do in BFS we can do the same
        things here, first we take a queue and add the root to the queue. Now will iterate till
        q is not empty. As we have to add all the element of any level to the level list, we need
        to iterate over all the element from the queue which are presnt on the same level.
        If the node is present then we can add the left and right sub-child to the queue, and
        add the node value to the level list.

        At last we will check the level list if not empty then we will add the list to a list.
        """
        que = deque()
        que.append(root)
        ans =[]

        while que:
            len_q = len(que)
            temp = []
            for _ in range(len_q):
                node = que.popleft()

                if node:
                    temp.append(node.val)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            if temp:
                ans.append(temp)
        return ans        