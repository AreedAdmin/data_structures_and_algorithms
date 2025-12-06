def power(x, n):
    """
    Calculates x raised to the power of n (x^n) recursively.
    Assume n is a non-negative integer.
    
    Example:
    power(2, 3) -> returns 8 (2 * 2 * 2)
    power(5, 0) -> returns 1
    """
    # TODO: Write your code here
    if n==1:
        return x

    if n == 0:
        return 1

    base = x**x

    return x * power(x,n-1)
    
    
y = power(5, 0)
print(y)