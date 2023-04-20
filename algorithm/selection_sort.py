def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [5, 3, 7, 1, 2, 8, 10, 4, 9, 6]

selection_sort(arr)

print(arr)