import sys

arr =[]
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split(" "))
    arr.append([a, b])

arr.sort()

for i in range(0, len(arr), 1):
    for j in range(i+1, len(arr), 1):
        if j >= len(arr):
            continue
        if arr[i][1] - arr[j][0] == 0:
            arr[i][1] = arr[j][1]
            del arr[j]
            continue

print(len(arr))