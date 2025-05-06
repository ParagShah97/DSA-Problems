# https://leetcode.com/problems/copy-list-with-random-pointer
# Time complexity: O(2N) =O(N)
# Space complexity: O(N)

# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Intuition:
        We simple do it in 2 passes, in first we will create a totally new LL also we will store the 
        mapping from old node to a new node against it. In first pass we just connect the new LL with
        next pointer.
        In second pass we will check if the random pointer in orignal LL is NULL then we assign NULL
        in the copy node random pointer. Else we will assign the mapped(copy node) to the random 
        pointer in the copy LL.
        '''

        # Brute force
        oldToNew = {}
        dummy = Node(0)
        first = dummy
        start = head
        # First pass we will create the copy LL and store the mapped from old to copy in dict.
        # and attach the copy LL with next pointer.
        while start:
            copy = Node(start.val)
            first.next = copy
            oldToNew[start] = copy
            start = start.next
            first = first.next
        
        start = head
        first = dummy.next
        # Agian we will start from the beginning, this time we will map the random pointer.
        # We will take the old node value from the start.random pointer and get the copy node against
        # it, that we just assign to new LL random pointer. 
        while start:
            if not start.random:
                first.random = None
            else:
                first.random = oldToNew[start.random]
            start = start.next
            first = first.next
        
        return dummy.next