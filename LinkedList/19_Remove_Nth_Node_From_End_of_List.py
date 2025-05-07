# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Time Complexity
# Space Complexity

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Intuition: 
        Approach 1:
        Brute froce approach, we first count the number of nodes, that is lenght of the linked list,
        once done, we can find the element we need to remove from the front, so consider we LL len = 5
        and n = 2(from back), then we need to len - n - 1 = 5-2-1 = 2, so we have to iterate 3 (0,1,2)
        times from the start again 1->2->3-x->5 (we do pointer.next = pointer.next.next).
        This way we remove the correct node.
        Corner cases, 
        Consider we have only 1 element then we can remove (i.e count = 1) by returning None.
        Consider count = 5 and n also = 5 then we can return head.next.

        Approach 2:
        2 pointer approach, we keep the distance between 2 pointer = n+1, that means once the second 
        pointer reaches to the end the first pointer will be at node just before the node need to be
        deleted, then we just do  first.next = first.next.next and return the start (dummy) node. 
        '''
    #     start = head
    #     count = 0
    #     # Iterate to count the lenght of the LL.
    #     while start:
    #         count += 1
    #         start = start.next
        
    #     # Corner case: if LL len = 1 then return None.
    #     if count == 1:
    #         return None
    # # Corner case: if n == count then we have to remove the first element, we can just return head.next
    #     if n == count:
    #         return head.next
    #     # By doing count -n -1 we can reach to the indexed element before removing element
    #     index_before_remove_ele = count - n-1
    #     #  Again start from the beginning
    #     start = head
    #     # Iterate till elem before.
    #     for _ in range(index_before_remove_ele):
    #         start =start.next        
    #     start.next = start.next.next       

    #     return head

        # Approach
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast:
            if n!=0:
                n-=1
                fast=fast.next
                continue
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next

        return dummy.next       