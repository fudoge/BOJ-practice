import sys
input =  sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().rstrip().split())
k = int(input().rstrip())

graph = [[] for _ in range(V+1)]
visited = [False] * (V + 1)
distance = [INF] * (V + 1)
         
for i in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))
         
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, V+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
         
def dijkstra(k):
    distance[k] = 0
    visited[k] = True
    for j in graph[k]:
        distance[j[0]] = j[1]
    for i in range(V-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
         
dijkstra(k)

for i in range(1, V+1):
    print(distance[i])
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
         