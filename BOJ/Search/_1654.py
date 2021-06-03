# 랜선 자르기
def check_count(origin, target):
    cnt = 0
    while origin > target:
        cnt += 1
        origin -= target

    return cnt


N, M = map(int, input().split())
a = []

for _ in range(N):
    a.append(int(input()))

start = 1
end = max(a)

while start <= end:
    total = 0

    mid = (start + end) // 2

    for i in a:
        total += i//mid

    if total >= M:
        start = mid + 1
    else:
        end = mid - 1


print(end)

