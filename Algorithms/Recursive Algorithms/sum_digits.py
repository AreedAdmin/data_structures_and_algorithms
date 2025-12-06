def sum_digits(n):
    """
    Recursively calculates the sum of all digits in a non-negative integer n.
    
    Example:
    sum_digits(123) -> returns 6 (because 1 + 2 + 3 = 6)
    sum_digits(45)  -> returns 9
    """
    # TODO: Write your code here
    if n ==0:
        return n

    last_digit=n%10
    
    return last_digit + sum_digits(n//10)

x=sum_digits(45)
print(x)