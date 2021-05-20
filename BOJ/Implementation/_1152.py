a=list(input().split(' '))
cnt=0

for i in a:
    if len(i)>0:
        cnt += 1

print(cnt)