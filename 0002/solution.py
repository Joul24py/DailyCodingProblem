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