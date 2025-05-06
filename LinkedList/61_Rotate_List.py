# https://leetcode.com/problems/rotate-list
# Time Complexity: O(2N)=O(N)
# Space Complexity: O(1)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Intuition:
        First we check if the LL is empty then just return head.
        Then we iterate to find the lenght of the LL and then we can update k
        value to k%len.

        If k == 0 the we just return head, no need of rotation.

        Next we keep fast and slow pointer, iterate till fast resached to end.
        we only move fast till k!=0 then we move both slow and fast pointer.

        Slow pointer will point to a node after which nodes will be rotated
        So, we keep new start to point slow.next and make slow.next =None
        then we iter from new start till end and last node next = head.
        This way we roated the nodes after slow.next to initial and 
        all the nodes till slow will attach to the last,and we already 
        made slow.next = None.
        """

        start=head
        ln=0

        # If the lenght of LL =0 then return head
        if not head:
            return head

        # Cal the lenght of LL
        while start:
            ln+=1
            start=start.next
        # Get the actual rotation value.
        k=k%ln
        # If k = 0 then just return head.
        if k == 0:
            return head

        fast=head
        slow=head
        # This way our slow pointer will reach to a point after which all the
        # values will going to rotate.
        while fast.next:
            if k!=0:
                fast=fast.next
                k-=1
                continue
            fast=fast.next
            slow=slow.next

        # slow's next pointer will be a new starting.
        newStart = itr = slow.next
        slow.next = None
        
        # new starting last node next value assign to head (initial start of LL)
        while itr.next:
            itr = itr.next

        itr.next=head

        return newStart