

def quick_sort(u_list):

    n = len(u_list)

    if n <= 1:
        return u_list

    #define pivot
    pivot=u_list.pop() #last item default

    items_greater=[]
    items_lower=[]

    for i in u_list:
        if i > pivot:
            items_greater.append(i)
        else:
            items_lower.append(i)
    return(quick_sort(items_lower)+[pivot]+quick_sort(items_greater))

u_list=[3,5,6,3,2,6,7,8,5,3,3,325,77,5442,6]




