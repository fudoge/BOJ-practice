import sys

def dfs(x, y):
    if 0 <= x < m and 0 <= y < n and graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

def putworm():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(j, i) == True:
                cnt += 1
    return cnt
    
t = int(sys.stdin.readline().rstrip())

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[n-y-1][x] = 1
    print(putworm())

