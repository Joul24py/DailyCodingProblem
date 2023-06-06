Implementation attempt in Python

Trying to solve the problem even with the bonus I thought that addition is commutative (which basically means that $a + b = b + a$) so this can help to not code a double ```for``` and check every possible combination as the following example:

```python
numbers = [1, 2, 3]
k = 7

for i in range(numbers):
    for j in range(numbers):
        if(k == (i + j)):
            return true
return false

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