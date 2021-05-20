num=int(input())
cnt=1

if num<10:
    num *= 10

temp=num

while True:
    first = temp % 10
    second = temp // 10

    temp = (first*10 + ((first+second)%10))
    if temp == num:
        break
    else:
        cnt += 1

print(cnt)