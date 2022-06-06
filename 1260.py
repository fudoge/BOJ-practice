import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
def bfs(graph, v, visited):
    queue = deque([v])
    
    visited[v] = True
    
    while queue:
        a = queue.popleft()
        print(a, end =" ")
        
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()
    
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)
dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)