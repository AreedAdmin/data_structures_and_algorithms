def flatten_list_deep(list_of_lists):
    """
    Recursively flattens a list of lists *of any depth* into a single list that contains all items of all sublists of list_of_lists.
    
    Parameter:
        list_of_lists: a list containing either integers or sublists. 
        The sublists may contain further integers and sublists, to arbitrary depth.  
    
    Returns: 
        a single list containing all items in the sublists, in order.
    
    Example:
    >>> flatten_list_deep([[1, 4, 6], [[3, [2]], 5, 2]])
    [1, 4, 6, 3, 2, 5, 2]
    """
    flat_list=[]

    for i, value in enumerate(list_of_lists):

        if isinstance(value, int):
            flat_list+=[value]
        
        if isinstance(value,list):
            result=flatten_list_deep(list_of_lists[i])
            flat_list+=result
    
    return flat_list

data=[[1, 4, 6], [[3, [2]], 5, 2]]
print(flatten_list_deep(data))