## Personal implementation attempt in Python

I think this implementation doesn't reach a solution in linear time when the length of the input increases. Anyways, my proposal is the following:

In order to solve this problem, first I'm going to re-order the array positioning every element that can be paired with its position as a bijection (the number $1$ in the first position, the number $2$ in the second position, so the number $n$ in the $n$-th position) since if the array has only different positive integer number then, the array would have from the $1$ to the value equals to the length of the array.

The previous case would return $n + 1$ as a result.

But having just a non positive integer number or a duplicate value would break the previous bijection. In this case, this number would take the place of a positive number that will be missing in the bijection.

So in this case, if we pair the number $n$ in the $n$-th position, I'm going to have a position in the array not corresponding to the value in it.

So I'm proposing a code to sort the array and then search for a hypothetical breaking bijection. Otherwise the bijection wouldn't be disrupted so I can return the $n + 1$ result.

My proposed code with the previous analysis is the following:

```python
def DCP4(nums = [3, 4, -1, 1]):
    n = len(nums)

    # Re-ordering the values to their hypothetical correct positions according to the proposed bijection
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Now searching the case when the bijection breaks
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If the bijection doesn't get broken, then the next positive is n + 1
    return n + 1
```