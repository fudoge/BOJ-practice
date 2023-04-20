def dfs(graph, v, visited):
    visited[v] = True#방문
    print(v, end=' ')

    for i in graph[v]:#스택 맨 위에 있는 노드에 대해서:
        if not visited[i]:#방문하지 않는 인접 노드 스택에 넣기
            dfs(graph, i, visited)
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
dfs(graph, 1, visited)