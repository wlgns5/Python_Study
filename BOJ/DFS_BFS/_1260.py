# DFS와 BFS
from collections import deque

def dfs(x):
    print(x, end=' ')
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


def bfs(x):
    q = deque([x])
    visited[x] = True

    while q:
        y = q.popleft()
        print(y, end=' ')
        for i in graph[y]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
