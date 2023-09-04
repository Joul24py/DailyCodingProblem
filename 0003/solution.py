class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def serialize(self):
        # Caso: Cuando la raíz no tienen ningún hijo
        if (self.left == None) and (self.right == None):
            return '(' + str(self.val) + '()())'
        
        # Caso: Cuando la raíz tiene sólo el hijo izquierdo
        if (self.left != None) and (self.right == None):
            return '(' + str(self.val) + str(self.left.serialize()) + '())'
        
        # Caso: Cuando la raíz tiene sólo el hijo derecho
        if (self.left != None) and (self.right == None):
            return '(' + str(self.val) + "()" + str(self.right.serialize()) + ')'
        
        # Caso: Cuando la raíz sí tiene ambos hijos
        return '(' + str(self.val) + str(self.left.serialize()) + str(self.right.serialize()) + ')'
    #def deserialize():
        
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(node.serialize())

#assert deserialize(serialize(node)).left.left.val == 'left.left'