# https://leetcode.com/problems/reorder-list/
# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        Intuition:
        We need to multiple steps to complete this question.
        1) First find the mid with slow/fast pointer, slow will point to the
        mid of the Linked List.
        2) Now, we take the slow pointer position and reverse the remaining 
        linked list.
        3) Now we put first prt and put it on head & second put it on last(after
        reverse it will be first node of the reverse linked list.)
        4) Now alterantingly put the nodes with first and second ptr.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1            
            first = temp1
            second = temp2