# https://leetcode.com/problems/reverse-linked-list/
# Time Complexity: O(N)
# Space Complexity: O(1)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
        We will keep prev as None, current points to head,
        then we iterate till cur != None.
        At every step we keep the next node in next pointer.
        Then we assign cur.next to prev, move prev to cur
        and cur to next, same goes on in every cycle.
        At last we return prev.
        """

        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        return prev