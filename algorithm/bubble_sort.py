def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

arr = [4, 3, 2, 7, 5, 9, 10, 1, 6, 8]

bubble_sort(arr)

print(arr)