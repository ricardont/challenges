#binary search treee
class Node:
    def __init__(self, key):
        self.key   = key 
        self.right = None 
        self.left  = None 

def insertNode(node,key):
    if node is None:
        return Node(key)
    if key >= node.key:
        node.right = insertNode(node.right,key)
    else:
        node.left = insertNode(node.left,key)
    return node
        


class Draw:
    def __init__(self, tree):
        self.tree = new_tree
        self.array   = [45, 15, 79, 90, 10, 55, 12, 20, 50] 
        self.html = generate_html(tree) 
        
    def generate_html(root):
        if root is None:
            return ''
        html = f'<div class="node">{root.value}</div>'
        html += generate_html(root.left)
        html += generate_html(root.right)
        return html
    
items_tree = [45, 15, 79, 90, 10, 55, 12, 20, 50]     
new_tree = None
for n in items_tree:
    new_tree = insertNode(new_tree, n)   
Draw(new_tree)     