# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Time Complexity O(N)
# Space Complexity O(N)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
from typing import List


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Intuition:
        It's interesting problem, here we need to traverse in BFS way from the
        target. But in tree we cannot traverse from child to parent, this issue
        can be resolved by using a seperate inorder traversal and make a reverse
        mapping from child to parent in a seperate dict.
        After that we can do a normal BFS traversal from the the target node, using
        queue.
        """

        # Mapping child to parent.
        parentMap = {}

        # DFS traversal to make the mapping from child to parent.
        def dfs(node):
            if not node:
                return            
            if node.left:
                parentMap[node.left] = node
                dfs(node.left)
            if node.right:
                parentMap[node.right] = node
                dfs(node.right)
        dfs(root)

        # Now start BFS from target node
        # Keep a queue, vis array
        q = deque()
        vis = set()
        vis.add(target.val)
        q.append(target)
        # For levels
        coverage = 0
        # BFS
        while q:
            # Break if we reach coverage equals to k 
            if coverage == k:
                break
            l = len(q)

            for _ in range(l):
                cur = q.popleft()

                # Left
                if cur.left and cur.left.val not in vis:
                    q.append(cur.left)
                    vis.add(cur.left.val)
                # Right
                if cur.right and cur.right.val not in vis:
                    q.append(cur.right)
                    vis.add(cur.right.val)
                # Parent
                if cur in parentMap and parentMap[cur].val not in vis:
                    q.append(parentMap[cur])
                    vis.add(parentMap[cur].val)
            coverage+=1
        # return the list of all the node values from the queue.
        return [itm.val for itm in q]