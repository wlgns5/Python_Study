# 토마토
from collections import deque


def tomatoconditioncheck():
    for i in range(M):
        for j in range(N):
            if a[i][j] == 0:
                return False

    return True

N, M = map(int, input().split())
a = []
for _ in range(M):
    a.append(list(map(int, input().split())))

q = deque()

for i in range(M):
    for j in range(N):
        if a[i][j] == 1:
            q.append((i, j))


while q:
    x, y = q.popleft()

    if (x + 1) < M:
        if a[x + 1][y] == 0:
            q.append(((x + 1), y))
            a[x + 1][y] = a[x][y] + 1
    if (x - 1) >= 0:
        if a[x - 1][y] == 0:
            q.append(((x - 1), y))
            a[x - 1][y] = a[x][y] + 1
    if (y + 1) < N:
        if a[x][y + 1] == 0:
            q.append((x, (y + 1)))
            a[x][y + 1] = a[x][y] + 1
    if (y - 1) >= 0:
        if a[x][y - 1] == 0:
            q.append((x, (y - 1)))
            a[x][y - 1] = a[x][y] + 1

result = -2
check_tot = False

for i in a:
    for j in i:
        if (j == 0):
            check_tot = True
        result = max(result, j)

if check_tot:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
