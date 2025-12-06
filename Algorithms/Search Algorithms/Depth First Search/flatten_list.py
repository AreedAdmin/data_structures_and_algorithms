def flatten(nested_list):
    """
    Takes a nested list of arbitrary depth and returns a 
    single, one-dimensional list of all integers.

    Example:
    data = [1, [2, [3, 4], 5], 6]
    flatten(data) -> [1, 2, 3, 4, 5, 6]
    """
    
    flat_list=[]

    for i, value in enumerate(nested_list):

        if isinstance(value, int):
            flat_list+=[value]

        if isinstance(value,list):
            result=flatten(nested_list[i])
            flat_list += result

    return flat_list
data = [1, [2, [3, 4], 5], 6]
print(flatten(data))