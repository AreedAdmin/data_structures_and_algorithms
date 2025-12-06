def find_first_odd(nested_list):
    """
    Recursively searches for the FIRST odd integer in a nested list
    and returns the list of indices (path) to reach it.
    If no odd number is found, returns None.

    Example:
    data = [2, [4, 8], [6, [10, 7], 12]]
    find_first_odd(data) -> [2, 1, 1]
    
    # Logic trace:
    # index 2 -> [6, [10, 7], 12]
    # index 1 -> [10, 7]
    # index 1 -> 7 (It is odd!)
    """
    # TODO: Write your code here
    for i, value in enumerate(nested_list):
        
        if isinstance(value, int) and (value % 2 == 1):
            return [i]
        
        if isinstance(value, list):
            result = find_first_odd(nested_list[i])

            if result is not False:
                return [i] + result

    return False
        


        
        
data = [12, [4, 5], [6, [10, 7], 12]]
print(find_first_odd(data))