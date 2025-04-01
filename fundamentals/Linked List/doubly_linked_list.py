# Doubly Linked List
class doublyNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, node, position):
        if position == 1:
            self.head = node
            return self.head
        else:
            curr_position=1
            curr = self.head
            while curr and curr_position < position-1:
                curr = curr.next
                curr_position += 1
            if curr:
                temp = curr.next
                curr.next = node
                node.prev = curr
                node.next = temp
        return self.head
    
    def insert_node_at_end(self, node):
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = node
        node.prev = curr
        return self.head
    
    def traverse_list(self):
        curr = self.head
        while curr:
            print("Node: ", curr.val)
            curr = curr.next
    
    def update_node(self, val, new_val):
        curr = self.head
        while curr and curr.val!=val:
            curr = curr.next
        curr.val = new_val
        return self.head
    
    def length_of_ll(self):
        len=0
        curr = self.head
        while curr:
            curr=curr.next
            len+=1
        return len
    
    def delete_node(self, val):
        curr = self.head
        if curr.val==val:
            self.head = self.head.next
            return
        while curr and curr.val!=val:
            curr=curr.next
        curr.prev.next = curr.next
        return self.head
        

    def delete_node_at_index(self, index):
        curr_index=0
        curr = self.head
        if index==0:
            self.head=self.head.next
            return self.head
        while curr:
            if curr_index == index:
                curr.prev.next = curr.next
                return self.head
            curr=curr.next
            curr_index +=1
        
    


dll = DoublyLinkedList()
dll.insert_node(doublyNode(0),1)
dll.insert_node(doublyNode(1),2)
dll.insert_node(doublyNode(5),3)
dll.insert_node(doublyNode(3),4)
dll.traverse_list()

dll.insert_node_at_end(doublyNode(4))
dll.traverse_list()

print(dll.length_of_ll())

dll.update_node(5,2)
dll.traverse_list()

dll.delete_node(0)
dll.traverse_list()

dll.delete_node_at_index(2)
dll.traverse_list()

"""
Node:  0
Node:  1
Node:  5
Node:  3

Node:  0
Node:  1
Node:  5
Node:  3
Node:  4

5

Node:  0
Node:  1
Node:  2
Node:  3
Node:  4

Node:  1
Node:  2
Node:  3
Node:  4

Node:  1
Node:  2
Node:  4

"""


