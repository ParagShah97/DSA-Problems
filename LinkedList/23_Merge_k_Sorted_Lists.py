# https://leetcode.com/problems/merge-k-sorted-lists/
# Time Complexity: log(k)*O(N) = O(Nlog(k))
# Space Complexity: O(k)

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Intuition:
        First we will check if len(list) if equals 0 then return None.
        Then we will iterate till list len > 1.
        Here the main idea is we are merging 2 lists at a time till we have only
        one list is remaining in the list array.
        We will keep a temp list called mergedAdjcentList and we call merge2List
        utility function to merge two sorted list at a time.

        We can simple write the merge two sorted list function, merging 2 lists.
        update the megedAdjcent list into lists array
        At last return lists[0].
        """

        if len(lists) == 0:
            return None
        
        def merge2List(h1,h2):
            start = cur = ListNode()

            while h1 and h2:
                if h1.val < h2.val:
                    cur.next = h1
                    h1=h1.next
                else:
                    cur.next = h2
                    h2=h2.next
                cur=cur.next
            cur.next = h1 or h2

            return start.next

        while len(lists) > 1:
            mergedAdjcentList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedAdjcentList.append(merge2List(l1,l2))
            lists=mergedAdjcentList
        
        return lists[0]