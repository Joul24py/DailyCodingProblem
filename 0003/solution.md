## Personal implementation attempt in Python

The implementation done in Python was achieved using the Python lists. I thought that could be a good idea serializing the binary tree as a list with always three members except when the node is None type, which would return an empty list (in other words, a list with length zero)

As a first step, serializing as a list was a process implemented as a recursive function to serialize a left or right node when this hasn't a None type value stored:

```python
def serialize(node):
    response = [node.val]
    # Analyzing left node
    if (node.left == None):
        response.append([])
    else:
        response.append(serialize(node.left))
    
    # Analyzing right node
    if (node.right == None):
        response.append([])
    else:
        response.append(serialize(node.right))
    
    return response
```

So if we use the node example in the problem:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
```

The result of passing this object through the ```serialize``` function would be the following:

```
['root', ['left', ['left.left', [], []], []], ['right', [], []]]
```

The result is always a list with length 3 except when the node doesn't have subnodes. Then, the subnodes are an empty list.

Then, as a second step, deserializing this result would check recursively if a left or right attribute has a length equal to zero. This ends the recursive function assigning to this subnode the None type value. Otherwise the function will enter as a recursive function to analyze the sublist:

```python
def deserialize(node):
    response = Node(node[0])
    
    # Analyzing left node
    if len(node[1]) == 0:
        response.left = None
    else:
        response.left = deserialize(node[1])
    
    # Analyzing right node
    if len(node[2]) == 0:
        response.right = None
    else:
        response.right = deserialize(node[2])
    
    return response
```