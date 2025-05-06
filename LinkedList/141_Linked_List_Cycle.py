# https://leetcode.com/problems/linked-list-cycle
# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Intuition:
        We can use the idea of slow and fast pointer. Slow pointer will move one step and fast pointer
        will move 2 steps at a time, if there is a cycle within the list then slow will point to fast
        after some iteration. If there is no cycle then the fast pointer will come to the end of the
        list, and last will return False after iteration end.
        '''
        
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False