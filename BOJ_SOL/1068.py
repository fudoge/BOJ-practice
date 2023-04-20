import sys
input = sys.stdin.readline
#입력값 받기와 기본 그래프 생성
n = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())
graph = [[] for _ in range(n)]
#노드의 부모 정보들로 인접리스트 만들기
for i in range(n):
    if nodes[i] != -1:
        graph[nodes[i]].append(i)
#그래프에서 노드 제거하기
def delete(node):
    for i in graph[node]:
        delete(i)
    graph[node] = []
    for i in range(n):
        if node in graph[i]:
            graph[i].remove(node)

delete(del_node)

# 루트 노드를 찾는 함수
def find_root(nodes):
    return nodes.index(-1)

# 루트 노드부터 탐색하여 리프 노드의 개수를 계산
def count_leaf(graph, v):
    if len(graph[v]) == 0:
        return 1
    cnt = 0
    for i in graph[v]:
        cnt += count_leaf(graph, i)
    return cnt

#루트를 찾고, 루트를 없애는 문제라면 바로 0을 반환하게 함
root = find_root(nodes)
print(count_leaf(graph, root) if del_node != root else 0)
