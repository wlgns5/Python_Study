# 숫자 카드2
from collections import Counter
def binary_search(a, x, start, end):

    if start > end:
        return False

    mid = (start + end) // 2

    if a[mid] == x:
        return mid

    elif a[mid] > x:
        return binary_search(a, x, start, mid-1)

    else:
        return binary_search(a, x, mid+1, end)


N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
result = [0] * M

a.sort()
a = Counter(a)

for i in b:
    print(a[i], end=" ")