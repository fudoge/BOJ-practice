import sys
from collections import deque

queue = deque([])
graph = []
day = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a >= 0 and a<n and b>=0 and b<m and graph[a][b] == 0:
                graph[a][b] = graph[x][y] + 1
                queue.append([a, b])

m, n = map(int, sys.stdin.readline().rstrip().split())
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day-1)
