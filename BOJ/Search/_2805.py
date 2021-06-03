# 나무 자르기

N, M = map(int, input().split())
a = list(map(int, input().split()))

start = 1
end = max(a)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in a:
        if i > mid:
            total += (i - mid)

    if total >= M:
        start = mid + 1
    else:
        end = mid - 1


print(end)


