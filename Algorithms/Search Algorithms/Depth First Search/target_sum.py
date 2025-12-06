def contains(nested_list, target):
    """
    Searches for 'target' in 'nested_list'.
    Returns True if found, False otherwise.
    
    Example:
    contains([1, [2, [3, 4]], 5], 3) -> True
    contains([1, [2, [3, 4]], 5], 99) -> False
    """
    # TODO: Loop through the list
    # Check if item == target
    # Check if item is a list -> Recurse!
    # Important: What do you do with the result of the recursion?
    
    for i in nested_list:
        if i == target:
            return True

        if isinstance(i, list):
            found = contains(i, target)
            if found == True:
                return True
        
        
    return False

x=contains([1, [2, [3, 4]], 5], 6)
print(x)