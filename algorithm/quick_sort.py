def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left_arr,  right_arr,  equal_arr = [], [], []
    
    for i in arr:
        if i > pivot:
            right_arr.append(i)
        elif i < pivot:
            left_arr.append(i)
        else:
            equal_arr.append(i)

    return quick_sort(left_arr) + equal_arr + quick_sort(right_arr)

arr = [1, 6, 3, 9, 10, 2, 5, 7, 4, 8]

print(quick_sort(arr))