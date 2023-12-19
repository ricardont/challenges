#binary search treee
class Node:
    def __init__(self, key):
        self.key   = key 
        self.right = None 
        self.left  = None 

def insertNode(node,key):
    if node is None:
        print(key)
        return Node(key)
    if key >= node.key:
        print(' -> ')
        node.right = insertNode(node.right,key)
    else:
        print(' <- ')
        node.left = insertNode(node.left,key)
    return node
        
items_tree = [45, 15, 79, 90, 10, 55, 12, 20, 50]
new_tree = None
for n in items_tree:
    new_tree = insertNode(new_tree, n)
print(new_tree.key)    
print(new_tree.right.key)    
print(new_tree.right.left.key)    
print(new_tree.right.left.left.key)    
# print(new_tree.right.left.key)    
# print(new_tree.right.left.left.key)    
#Pseudocode
# - Create Model to hold node Info Key, left , right branch
# - Method to insert node in any given tree structure, 
#      receives node object or 'root' and new key value
#        if root node is none return and instance of node
#        else if new value is ge than root value insert root right attribute node new value instance
#        else if new value insert to root left  attribute node new value instance
#       return root 
# - Loop throug array to populate bst calling previous insert method

