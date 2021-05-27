# 단지번호 붙이기
import sys


def dfs(x, y):
    global result
    if graph[x][y] == 1:
        result += 1
        graph[x][y] = 0
    else:
        return

    if x+1<n:
        dfs(x+1, y)
    if y+1<n:
        dfs(x, y+1)
    if x-1>=0:
        dfs(x-1, y)
    if y-1>=0:
        dfs(x, y-1)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = 0
a = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result = 0
            dfs(i, j)
            a.append(result)
            cnt += 1

print(cnt)
a.sort()
for i in a:
    print(i)
