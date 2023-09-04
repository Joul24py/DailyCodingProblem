## Personal implementation attempt in Python

Trying to solve the problem even with the bonus I thought that addition is commutative (which basically means that $a + b = b + a$) so this can help to not code a double ```for``` and check every possible combination as the following example:

```python
numbers = [1, 2, 3]
k = 7

for i in range(numbers):
    for j in range(numbers):
        if(k == (i + j)):
            return True
return False
```

So trying to not execute repeated operations, the idea is iterate the second ```for``` only in the not iterated numbers by the first ```for``` resulting in the next function:

```python
def DCP1(numbers = [10, 15, 3, 7], k = 17):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            print(str(numbers[i]) + " + " + str(numbers[j]))
            if(k == (numbers[i] + numbers[j])):
                return True
    return False
```

---

## Correction thanks to discussion with friends

Thanks to college friends who talked with about this problem, we tried to improve the implementation.

If a sum of two numbers of the list results in $k$ then $k - a = b$ where $a$ and $b$ are part of the given list of numbers.

So using a set data structure, we can append to the set the number $a$ if $b$ is not in the set

This makes the implementation in one pass (iterating the $a$ number) and as the commutative property of addition: $a + b = b + a$ if it exists a pair of numbers that its addition results in $k$ when the iteration reaches the second number, the first number will be in the set and the substraction will find it in the set, so the result will be true.

The code is the following:

```python
def DCP1(numbers = [10, 15, 3, 7], k = 17):
    complements = set()
    
    for a in numbers:
        b = k - a
        
        if b in complements:
            return True
        
        complements.add(a)
    return False
```