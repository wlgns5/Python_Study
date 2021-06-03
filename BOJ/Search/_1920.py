# 수 찾기
def binary_search(array, target, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

a.sort()


for i in b:
    if binary_search(a, i, 0, n - 1):
        print(1)
    else:
        print(0)


