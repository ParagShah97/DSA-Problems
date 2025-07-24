# https://leetcode.com/problems/linked-list-cycle-ii
# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
        Here we need to find the starting point of the loop in a linkedList.
        
        First we can use slow and fast pointer approach to check if there exist a loop.
        If no loop exist then we can return None, as there is no starting.
        Here we can use the bool to check for the cycle.

        Once we get the slow==fast pointer then we take another pointer say cur,
        start cur from head and move slow and cur 1 step at a time and the point 
        both meet return either start or cur.
        """
        slow, fast = head, head
        isCycle=False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isCycle = True
                break
        
        if not isCycle:
            return None
        
        cur=head
        while cur != slow:
            cur=cur.next
            slow=slow.next
        return cur