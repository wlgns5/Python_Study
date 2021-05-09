# 덩치
n=int(input())
inputa=[]
result=[]

for _ in range(n):
  x, y = map(int, input().split(' '))
  inputa.append((x, y))

for i in range(n):
  rank=1
  for j in range(n):
    if i==j:
      continue

    # 덩치가 큰 경우
    if inputa[i][0]<inputa[j][0] and inputa[i][1]<inputa[j][1]:
      rank += 1
    
    # 덩치가 같은 경우
    else:
      continue

  print(rank)

