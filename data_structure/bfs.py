from collections import deque

def bfs(graph, start, visited):
    q = deque([start])#시작 노드를 큐에 넣는다
    visited[start] = True#방문처리한다
    while q:#큐에 노드가 있는 동안:
        v = q.popleft()#제일 먼저 들어온 노드를 빼서
        print(v, end = ' ')
        for i in graph[v]:#인접 노드들 중 방문하지 않은 노드들을 큐에 넣고 방문처리한다
            if not visited[i]:
                q.append(i)
                visited[i] = True

#그래프의 정보(인접 노드들)
graph = [[],
         [2, 3, 4],
         [1, 5],
         [1, 7],
         [1, 8],
         [2, 6],
         [5],
         [3, 8],
         [4, 7]]
#방문 정보
visited = [False] * 9
#1부터 깊이우선탐색
bfs(graph, 1, visited)
