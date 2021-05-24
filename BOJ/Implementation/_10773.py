a=[]

n = int(input())

for _ in range(n):
    num = int(input())
    if num != 0:
        a.append(num)
    else:
        a.pop()

print(sum(a))