def reverse_string(s):
    """
    Returns the reverse of the input string s.
    
    Example:
    reverse_string("hello") -> returns "olleh"
    reverse_string("a") -> returns "a"
    """
    # TODO: Write your code here
    reverse=''
    if len(s) == 0:
        return s

    last_char=s[len(s)-1:]
    reverse+=last_char

    return last_char + reverse_string(s[:len(s)-1])
    

x=reverse_string("hello")
print(x)