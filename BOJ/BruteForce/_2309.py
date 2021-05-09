# 일곱 난쟁이
import itertools

arr=[]
for _ in range(9):
  arr.append(int(input()))

result = list(itertools.combinations(arr, 7))


for i in range(len(result)):
  sumarr=[]
  for j in range(7):
    sumarr.append(result[i][j])

  if sum(sumarr)==100:
    sumarr = sorted(sumarr)
    for k in sumarr:
      print(k)
    break


