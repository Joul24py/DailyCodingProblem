import numpy as np

def DCP2(numbers = [1, 2, 3, 4, 5]):
    product = np.prod(numbers)
    
    products = []
    for i in range(len(numbers)):
        products.append(int(product / numbers[i]))
    
    return products