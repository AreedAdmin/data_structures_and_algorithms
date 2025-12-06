def find_negative_path(nested_list):
    """
    Recursively searches for the FIRST negative number in a nested list
    and returns the list of indices (path) to reach it.
    If no negative number is found, returns None.

    Example:
    data = [1, [2, 3], [4, [5, -99], 6]]
    find_negative_path(data) -> [2, 1, 1]
    
    # Logic trace:
    # index 2 -> [4, [5, -99], 6]
    # index 1 -> [5, -99]
    # index 1 -> -99 (Found!)
    """
    # TODO: Write your code here
    # loop through the list
    for i, value in enumerate(nested_list):

    #check if we found the first negative number
        if isinstance(value, int) and value < 0:
            return [i]
    
    #otherwise we need to go further into the rabbit hole
        if isinstance(value,list):
            result = find_negative_path(nested_list[i])

            if result is not None:
                return [i] + result

    #if their is none 
    return None

    #then we return false or none
data = [1, [2, 3], [4, [5, -99], 6]]
print(find_negative_path(data))
