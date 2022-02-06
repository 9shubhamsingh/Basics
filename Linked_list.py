"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.

class ListNode:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:

   def __init__(self):
        self.head = None

   def push(self,new_data):

        new_node = ListNode(new_data)

        new_node.next = self.head

        self.head = new_node


   def append(self,new_data):

        new_node = ListNode(new_data)

        if self.head is None:
            self.head  = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

   def insert_after(self,prev_node,new_data):

        if prev_node is None:
            print ("The given previous node must inLinkedList. ")
            return

        new_node = ListNode(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

   def printList(self):
        temp = self.head

        while temp:
            print (temp.data,end = ' ')
            temp = temp.next




if __name__ == '__main__':
    

    # Start with the empty list
    llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
    llist.append(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insert_after(llist.head.next, 8)
 
    print ('Created linked list is:',)
    llist.printList()