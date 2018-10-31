
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root == None:
        return "null-"

    return root.val + "-" + serialize(root.left) + serialize(root.right)

def derserialize(node_list):
    value = node_list[0]
    node_list.remove(value)

    if value == "null":
        return None

    root = Node(value)
    root.left = derserialize(node_list)
    root.right = derserialize(node_list)
 

    return root
    
    
    
def deserialize_helper(s):
    node_list = s.split("-")
    node_list = node_list[0:len(node_list) - 1]
    print(node_list)
    return derserialize(node_list)

node = Node('root', Node('left', Node('left.left')), Node('right'))
s = serialize(node)
print(s)
print(deserialize_helper(s).left.left.val)


