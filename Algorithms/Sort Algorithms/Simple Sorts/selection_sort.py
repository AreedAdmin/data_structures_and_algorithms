def selection_sort(unordered_list):
    n = len(unordered_list)

    #loop through the list
    for i in range(n):
    #set the next value as the minimum this is our target
        minimum = i
        
    #create second loop
        for j in range(i+1,n):
            if unordered_list[j] < unordered_list[minimum]:
                #check for and find true minimum
                minimum = j
    
        #swap the minimum with the current i target
        unordered_list[i], unordered_list[minimum] = unordered_list[minimum], unordered_list[i]

    return print(unordered_list)


selection_sort([6,4,32,1,5,6,7,7,5,3,2,1])
    


    
            
