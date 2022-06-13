from collections import deque

def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    print(tickets[0])
    queue = deque([tickets[0]])
    visited[0] = True
    while queue:
        a, b = queue.popleft()
        answer.append(a)
        for i in range(1, len(tickets)):
            if tickets[i][0] == b and not visited:
                queue.append(tickets[i])
                visited[i] = True
    return answer

graph = input()
print(solution(graph))
