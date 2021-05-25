# 바이러스
from collections import deque

def bfs(x):
    q = deque([x])
    visited[x] = True
    global cnt
    cnt = 0

    while q:
        y = q.popleft()
        for i in graph[y]:
            if not visited[i]:
                q.append(i)
                cnt += 1
                visited[i] = True


n = int(input())
m = int(input())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
print(cnt)

