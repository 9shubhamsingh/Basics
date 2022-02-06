"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

# Python3 program to find the diameter of binary tree

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None



# The function Compute the "height" of a tree. Height is the
# number of nodes along the longest path from the root node
# down to the farthest leaf node.

def diameterOfBinaryTree(root) -> int:
	res = [0]

	def dfs(root):
		if not root:
			return -1
		left = dfs(root.left)
		right = dfs(root.right)

		res[0] = max(res[0],2 + left + right)

		return 1 + max(left,right)

	dfs(root)
	
	return res[0]





"""
def height(node):

	# Base Case : Tree is empty
	if node is None:
		return 0

	# If tree is not empty then height = 1 + max of left
	# height and right heights
	return 1 + max(height(node.left), height(node.right))

# Function to get the diameter of a binary tree
def diameter(root):

	# Base Case when tree is empty
	if root is None:
		return 0

	# Get the height of left and right sub-trees
	lheight = height(root.left)
	rheight = height(root.right)

	# Get the diameter of left and right sub-trees
	ldiameter = diameter(root.left)
	rdiameter = diameter(root.right)

	# Return max of the following tree:
	# 1) Diameter of left subtree
	# 2) Diameter of right subtree
	# 3) Height of left subtree + height of right subtree +1
	return max(lheight + rheight + 1, max(ldiameter, rdiameter))
"""

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
print(diameterOfBinaryTree(root))


