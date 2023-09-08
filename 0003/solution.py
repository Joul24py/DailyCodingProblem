class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def serialize(node):
    response = [node.val]
    # Analizando hijo izquierdo
    if (node.left == None):
        response.append([])
    else:
        response.append(serialize(node.left))
    
    # Analizando hijo derecho
    if (node.right == None):
        response.append([])
    else:
        response.append(serialize(node.right))
    
    return response

def deserialize(node):
    response = Node(node[0])
    
    # Analizando hijo izquierdo
    if len(node[1]) == 0:
        response.left = None
    else:
        response.left = deserialize(node[1])
    
    # Analizando hijo derecho
    if len(node[2]) == 0:
        response.right = None
    else:
        response.right = deserialize(node[2])
    
    return response

node = Node('root', Node('left', Node('left.left')), Node('right'))

assert deserialize(serialize(node)).left.left.val == 'left.left'