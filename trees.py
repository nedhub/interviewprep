#Each part of a tree is called a node.
#At the very top of the tree we have the root node
#great for modelling organizations
#benefit is the speed
#nodes with the same parents are called siblings
#descendants are everything below the node


#Binary search tree
#every node is greater than every node in its left subtree

#each node is less than every node in its right subtree


#Operations

#Insert
#Find
#Delete
#Get_size
#Traversals




#Insert

#Start at root
#Always insert as a leaf


#Find

#Start at root
#Return the data if found, or False if not found

#BST Delete

#3 possible cases:
#leaf node
#just delete the leaf node


#one child
#promote the child to the target node's position


#two children
#find the next higher node


#Get_size

#returns number of nodes. Works recursively


#size = 1
# + size(left subtree)





#Preorder Traversal

#Visit root before visiting the root's subtrees. 


#Inorder Traversal

#visit root between visiting the root's subtrees

#Gives values in sorted order.



#Advantages of Binary Search Tree

#Becuase of recursion, easy to implement
#Speed

#Insert, Delete, Find in O(h) = O(logn)


