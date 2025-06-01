# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
# Time Complexity: O(N)
# Space Complexity: O(N)


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
Inutuition:
Here we need to make the level connections, we can do it with the help of 
level order traversal.
At every level I am keeping the prev pointer initially Null, for each
level we for the elements in the queue (for that level), I am attaching 
the prev to the next pointer of the element pop from the queue.
Here I am inserting the right element first and then left element in the
queue.
"""

from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        if not root.left and not root.right:
            return root

        q = deque()
        q.append(root)

        while q:
            prev=None
            q_len = len(q)

            while q_len > 0:
                node = q.popleft()
                q_len -= 1

                if node:
                    node.next = prev
                    prev = node
                    # Check if right sub tree exists or not.
                    if node.right:
                        q.append(node.right) 
                    # Check if left sub tree exists or not.
                    if node.left:
                        q.append(node.left)
        return root