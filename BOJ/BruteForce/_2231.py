# 분해합
n=int(input())
INF=100000000
result=INF

for i in range(1, n):
  num=i
  cnt=i
  while True:
    cnt += num%10
    num //= 10
    if num<=0:
      break
  
  if cnt==n:
    result=min(i, result)

if result==INF:
  print("0")
else:
  print(result)

    

