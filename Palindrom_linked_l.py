"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""

class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class Solution:
	def isPalindrome(self, head) -> bool:
		nums = []

		while head:
			nums.append(head.data)
			head = head.next

	
		l,r = 0, len(nums)-1

		while l<=r:
			if nums[l] != nums[r]:
				return False
			l +=1
			r -=1
		return True




class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


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
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(1)

print ("Given Linked List")
llist.printList()
print("\n")
print(Solution().isPalindrome(llist.head))