'''
The Structure to aim for:
Check Base Case: Is length <= 1? Return list.
Find Midpoint: n // 2.
Recursion:
left_sorted = merge_sort(first_half)
right_sorted = merge_sort(second_half)
The Merge Logic:
Create three pointers: i (for left list), j (for right list), k (for main list) OR just a new list result.
While i is inside left list AND j is inside right list:
Compare, append smaller to result, increment pointer.
Crucial: After the loop, check if any items are left over in left or right and add them to the result.
Return: The combined list
'''

list1=[4,3,5,6,7,4,2,7,7,8,8,42,2]

n = len(list1)

if n <= 1:
    print(list1)

midpoint = n // 2

left_sorted = merge_sort(list1[:midpoint])
right_sorted = merge_sort(list1[midpoint:])

