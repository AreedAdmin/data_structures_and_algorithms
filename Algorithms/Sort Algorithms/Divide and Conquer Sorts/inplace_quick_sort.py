def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:

            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_inplace(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)

        quick_sort_inplace(arr, low, pi - 1)

        quick_sort_inplace(arr, pi + 1, high)


u_list = [3, 5, 6, 3, 2, 6, 7, 8, 5, 3, 3, 325, 77, 5442, 6]
quick_sort_inplace(u_list, 0, len(u_list) - 1)
