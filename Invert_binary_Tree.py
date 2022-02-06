"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Solution:
    def invertTree(self, root) -> Node:

    	if not root:
    		return None

    	root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)

    	return root

# Driver Code
"""
Constructed binary tree is
	     1
		/ \
	   2   3
	  / \
	 4	 5
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Function Call
print(Solution().invertTree(root))

