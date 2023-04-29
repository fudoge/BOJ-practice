def counting_sort(arr):
    max_num = max(arr)
    count = [0] * (max_num + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(max_num + 1):
        for j in range(count[i]):
            sorted_arr.append(i)

    return sorted_arr


arr = [10, 100, 3, 1]

print(counting_sort(arr))