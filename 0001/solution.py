def DCP1(numbers = [10, 15, 3, 7], k = 17):
    complements = set()
    
    for a in numbers:
        b = k - a
        
        if b in complements:
            return True
        
        complements.add(a)
    return False