N = int(input())
a = []

for _ in range(N):
    x, y = map(int, input().split())
    a.append((x, y))

a = sorted(a, key=lambda x: x[0])
a = sorted(a, key=lambda x: x[1])

cnt = 0
start_time = 0

for i in range(N):
    if a[i][0] >= start_time:
        start_time = a[i][1]
        cnt += 1

print(cnt)
