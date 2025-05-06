# https://leetcode.com/problems/merge-two-sorted-lists
# Time Complexity O(max(n,m))
# Space Complexity O(1)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        """
        Intuition:
        We can make a place holder node for a start, then we iterate till either of 
        the LL reach the end, at every cycle we will check if l1 cur or l2 cur
        value is smaller which ever is smaller assugn the temp node successor
        and goes on till we reah end of either of a LL.
        Later we just connect head1 or head2 to temp succesor as only one may have
        remaining element.
        """
        start = cur = ListNode()

        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        
        cur.next = head1 or head2
        return start.next