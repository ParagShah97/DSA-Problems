# https://leetcode.com/problems/add-two-numbers
# Time Complexity: O(MAX(m,n))
# Space Complexity: O(MAX(m,n))
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
        Intuition:
        Will create a temp node as a starter node.
        We keep a carry variable.
        First Iteration will iterate till (h1 and h1 either of one not reach the end)
        For every cycle we calculate sum h1.val h2.val+ carry
        And we store 10s bit in carry and one bit assign to the newly created node.
        Move the pointer respectively

        Second & Third Iteration, if length of either of the list is
        smaller then other then:

        iterate on them and do the same step like add the carry to the 
        current element and assign to new node and move the pointer.
        """
        itr=temp=ListNode(0)
        h1=l1
        h2=l2
        carry = 0
        while h1 and h2:
            sm = h1.val+h2.val+carry
            carry = sm//10
            node = ListNode(sm%10)
            itr.next = node
            itr = node
            h1=h1.next
            h2=h2.next

        while h1:
            sm = h1.val+carry
            carry = sm//10
            node = ListNode(sm%10)
            itr.next = node
            itr = node
            h1=h1.next

        while h2:
            sm = h2.val+carry
            carry = sm//10
            node = ListNode(sm%10)
            itr.next = node
            itr = node
            h2=h2.next

        if carry != 0:
            node = ListNode(carry)
            itr.next = node
        
        # print(temp)
        return temp.next        