
def insertion_sort(u_list):
    n = len(u_list)

    for i in range(1,n):
        while u_list[i-1] > u_list[i] and i >0:
            u_list[i-1],u_list[i]=u_list[i],u_list[i-1]
            i -=1 
#At the start of every new iteration, the for statement overwrites i with the next number in the sequence, ignoring the changed i value to inside the loop.
    return u_list


print(insertion_sort([45,3,6,2,5,45,4,3,2,234,2344,2,16]))

