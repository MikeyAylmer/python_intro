def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    total = []

    for num in nums:
        if isinstance(num, float):
            total.append(num)
            
            
    return sum(total)
        
    # or can return with a list comprehension like this.
    # return sum([num for num in nums if isinstance(num, float)])
    