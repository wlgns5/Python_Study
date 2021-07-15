from collections import deque

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        if x+1 < n:
            if temp[x+1][y] != 101:
                q.append((x+1, y))
                temp[x+1][y] = 101

        if x-1 >= 0:
            if temp[x - 1][y] != 101:
                q.append((x-1, y))
                temp[x - 1][y] = 101

        if y + 1 < n:
            if temp[x][y+1] != 101:
                q.append((x, y+1))
                temp[x][y+1] = 101

        if y - 1 >= n:
            if temp[x][y-1] != 101:
                q.append((x, y-1))
                temp[x][y-1] = 101

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

result = []
temp = []
for k in range(1, n):


    for i in range(n):
        for j in range(n):
            if temp[i][j] <= k:
                temp[i][j] = 101

    print(temp)
    print(a)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j] != 101:
                bfs(i, j)
                cnt += 1

    result.append(cnt)


print(result)