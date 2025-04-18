# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow.next
        prev=slow.next=None

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        start=head
        end=prev

        while end:
            tmp1,tmp2=start.next, end.next
            start.next=end
            end.next=tmp1
            start=tmp1
            end=tmp2

