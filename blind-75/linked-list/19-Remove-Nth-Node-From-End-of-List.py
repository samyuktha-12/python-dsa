# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """slow=fast=head
        i=0
        while i<n:
            fast=fast.next
            i+=1
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        
        slow.next=slow.next.next
        return head"""

        dummyNode = ListNode(0,head)
        slow=dummyNode
        fast=head
        i=0
        while i<n:
            i+=1
            fast=fast.next
        
        while fast:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next
        return dummyNode.next
        