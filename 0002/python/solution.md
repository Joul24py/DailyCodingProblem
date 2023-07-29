## Personal implementation attempt in Python

An easy implementation is doing a product of all numbers of the list and then in each position dividing it by that same position of the given array. This can be achieved with the following code:

```python
import numpy as np

def DCP2(numbers = [1, 2, 3, 4, 5]):
    product = np.prod(numbers)
    
    products = []
    for i in range(len(numbers)):
        products.append(int(product / numbers[i]))
    
    return products
```