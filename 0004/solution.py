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