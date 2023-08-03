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

## Correction thanks to discussion with friends

I told to some college friends this problem (but forcing them to not use division) and see what solution can we all give to the problem.

To the conclusion we came up was to make two products: one from the previous numbers from the current position and another from the upcoming numbers. We called this the *"left product"* and the *"right product"* (because when we write ```[0, 1, ... , i - 1, i, i + 1, ... , n - 1, n]``` we can see the numbers ```0``` to ```i - 1``` to the left of ```i``` and the numbers ```i + 1``` to ```n``` to the right of ```i```)

The easiest product to see was the left product, because of the traditional way we iterate, we can inicialize a product variable in 1 when starting to iterate the array. This variable will be (for now) the value in this same position but in the resulting array. Then we multiply this product variable by the current position as we move to the next member of the array. The product variable will acumulate the left product as it advances through the array.

Then this its going to happen like the left product but now iterating in a reverse way (starting from the last position and ending with the first position) doing a right product that will combine its result with the obtained with the left products.

With this approach we try to not use excessive iterations (in fact this approach will use only two iterations as other approaches used the same iterations as numbers in the input array).

The code is the following:

```python
def DCP2(numbers = [1, 2, 3, 4, 5]):
    n = len(numbers)
    products = [1] * n
    
    # Calculating left products
    left_product = 1
    for i in range(n):
        products[i] *= left_product
        left_product *= numbers[i]
    
    # Calculating right products
    right_product = 1
    for i in reversed(range(n)):
        products[i] *= right_product
        right_product *= numbers[i]
    
    return products
```