import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in  range(n)]

arr.sort()
room=[]
print("arr: ", arr)
heapq.heappush(room, arr[0][1])

for i in range(1, n):
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])
        print(room)
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
        print(room)

print(len(room))