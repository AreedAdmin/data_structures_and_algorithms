def find_path(nested_list, target):
    """
    Returns a list of steps to find the target.
    If not found, returns None.
    
    Example:
    find_path([1, [2, "apple"], 3], "apple") 
    -> [1, 1]  (Index 1, then Index 1 inside that)
    """
    for i, value in enumerate(nested_list):

        if value == target:
            return [i]
        
        if isinstance(value, list):
            result = find_path(value,target)
            
            if result is not None:
                return [i] + result
    

x=find_path([1, [2, "apple"], 3], "apple") 
print(x)