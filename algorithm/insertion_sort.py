def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

arr = [4, 7, 1, 8, 10, 9, 2, 5, 3, 4]

insertion_sort(arr)

print(arr)