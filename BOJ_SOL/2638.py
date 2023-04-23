from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = 0
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    q = deque([])
    q.append([0, 0])
    visited[0][0] = True

    while q:    #외부 공기 탐색
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: #외부 공기들을 -1로 칠한다.
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    graph[nx][ny] = -1
                    q.append([nx, ny])
    for i in range(n):  #visited 초기화
        for j in range(m):
            visited[i][j] = False
    q.append([0, 0])    #다시 0,0부터 탐색하며, 외부 공기와 인접한 치즈들은 인접한 수만큼 추가해준다
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])
                if graph[nx][ny] == 1:
                    for i in range(4):
                        mx = nx + dx[i]
                        my = ny + dy[i]
                        if graph[mx][my] == -1:
                            graph[nx][ny] += 1

while True:
    visited = [[False] * m for _ in range(n)]
    bfs()
    flag = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3: #외부 공기와 2면 이상 인접한 것들은 없애고,
                graph[i][j] = 0
                flag = 1
            elif graph[i][j] == 2: #하나만 인접한 것들은 다시 1로 바꿔주고,
                graph[i][j] = 1
            elif graph[i][j] == -1: #외부공기들도 초기화해준다.
                graph[i][j] = 0
    if flag == 1: #치즈가 녹은게 있으면 시간을 하나 늘린다
        time += 1
    else:
        break #더 녹이는게 없으면 종료.

print(time)