# 주유소
n = int(input())
load_length = list(map(int, input().split()))
value = list(map(int, input().split()))

result = 0
m = value[0]

for i in range(n-1):
    if value[i] < m:
        m = value[i]
    result += (load_length[i] * m)

print(result)

