# Singly Linked List
class singlyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def insert_node(self, node, position):
        if self.head:
            if position == 1:
                self.head= node
                node.next=self.head
                return self.head
            else:
                curr_position = 1
                curr = self.head
                while curr and curr_position < position-1:
                    curr=curr.next
                    curr_position += 1
                
                if curr: # this check is added so that if position is greater than the length of the ll, it doesn't throw error
                    node.next = curr.next
                    curr.next = node
                    return self.head
        
        else:
            self.head=node
            return self.head
        
    def insert_node_at_end(self,node):
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=node
        return self.head
        
        
    def traverse_linked_list(self):
        curr=self.head
        while curr:
            print("Node: ", curr.value)
            curr=curr.next

    def update_node(self, node, new_value):
        curr = self.head
        while curr.value!=node.value:
            curr=curr.next
        curr.value = new_value
        return self.head
    
    def length_of_linkedlist(self):
        len=0
        curr = self.head
        while curr:
            len+=1
            curr=curr.next
        return len
    
    def delete_node(self,value):
        curr=self.head
        if curr.value == value:
            self.head = self.head.next
            return self.head
        while curr.next:
            if curr.next.value == value:
                curr.next = curr.next.next
                return self.head
            curr=curr.next
    
    def delete_node_by_index(self,index):
        curr=self.head
        curr_index=0
        if index==0:
            self.head=self.head.next
            return self.head
        while curr.next and curr_index<index-1:
            curr=curr.next
            curr_index+=1
        curr.next=curr.next.next
        return self.head
        



sll = SinglyLinkedList()
sll.insert_node(singlyNode(1),1)
sll.insert_node(singlyNode(2),2)
sll.insert_node(singlyNode(3),3)
sll.traverse_linked_list()


sll.insert_node_at_end(singlyNode(4))
sll.traverse_linked_list()

sll.update_node(singlyNode(4),5)
sll.traverse_linked_list()

print(sll.length_of_linkedlist())

sll.delete_node(5)
sll.traverse_linked_list()

sll.delete_node_by_index(1)
sll.traverse_linked_list()

"""
Node:  1
Node:  2
Node:  3

Node:  1
Node:  2
Node:  3
Node:  4

Node:  1
Node:  2
Node:  3
Node:  5

4

Node:  1
Node:  2
Node:  3

Node:  1
Node:  3

"""

