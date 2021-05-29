# 미로탐색
from collections import deque
def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        if (x+1) < N:
            if arr[x+1][y] == 1:
                arr[x+1][y] = arr[x][y] + 1
                q.append(((x+1), y))

        if (x-1) >= 0:
            if arr[x - 1][y] == 1:
                arr[x - 1][y] = arr[x][y] + 1
                q.append(((x - 1), y))

        if (y + 1) < M:
            if arr[x][y + 1] == 1:
                arr[x][y + 1] = arr[x][y] + 1
                q.append((x, (y+1)))

        if (y - 1) >= 0:
            if arr[x][y - 1] == 1:
                arr[x][y - 1] = arr[x][y] + 1
                q.append((x, (y - 1)))


N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

bfs(0, 0)
print(arr[N-1][M-1])


