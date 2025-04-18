# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        dummyNode=ListNode(-1)
        current=dummyNode
        for node in lists:
            if node:
                heapq.heappush(heap,(node.val, id(node), node))

        while heap:
            _, _, node = heapq.heappop(heap)
            current.next=node
            current=current.next
            if node.next:
                heapq.heappush(heap,(node.next.val, id(node.next), node.next))
        
        return dummyNode.next
