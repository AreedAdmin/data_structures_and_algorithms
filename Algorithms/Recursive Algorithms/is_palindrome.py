def is_palindrome(s):
    """
    Returns True if the string s is a palindrome (reads the same forwards and backwards),
    otherwise returns False.
    
    Example:
    is_palindrome("racecar") -> returns True
    is_palindrome("hello")   -> returns False
    """
    # TODO: Write your code here

    if len(s) < 2:
        return True
    
    if s[:1] != s[len(s)-1:]:
        return False
    
    return is_palindrome(s[len(s)-(len(s)-1):len(s)-1])

x=is_palindrome("")
print(x)
