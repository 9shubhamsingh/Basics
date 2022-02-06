"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to reverse the linked list
	def reverse(self,head):
		
		# If head is empty or has reached the list end
		if head is None or head.next is None:
			return head
  
        # Reverse the rest list
		rest = self.reverse(head.next)
  
        # Put first element at the end
		head.next.next = head
		head.next = None
  
        # Fix the header pointer
		return rest




	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end = ' ')
			temp = temp.next


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print ("Given Linked List")
llist.printList()
llist.head = llist.reverse(llist.head)
print ("\nReversed Linked List")
llist.printList()


