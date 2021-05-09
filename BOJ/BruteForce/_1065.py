# 한 수

n=input()
i_n=int(n)
cnt=0

for i in range(1, (i_n+1)):
  if i < 100:
    cnt+=1
  else:
    tempstr=str(i)
    if (int(tempstr[2])-int(tempstr[1]))==(int(tempstr[1])-int(tempstr[0])):
      cnt+=1

print(cnt)


