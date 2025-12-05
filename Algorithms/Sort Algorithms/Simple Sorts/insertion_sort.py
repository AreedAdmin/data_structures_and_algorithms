
def insertion_sort(u_list):
    n = len(u_list)

    for i in range(1,n):
        while u_list[i-1] > u_list[i]:
            u_list[i-1],u_list[i]=u_list[i],u_list[i-1]
            i -=1
    return u_list


print(insertion_sort([45,3,6,2,5,45,4,3,2,234,2344,2,16]))

