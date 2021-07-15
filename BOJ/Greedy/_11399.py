# ATM

n = int(input())
a = list(map(int, input().split()))

a.sort()

cnt = 0
for i in range(n+1):
    for j in range(i):
        cnt += a[j]

print(cnt)