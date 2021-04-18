# p180
N = int(input())

arr=[]
for i in range(N):
  temp=input().split()
  arr.append((temp[0], int(temp[1])))

arr = sorted(arr, key=lambda x: x[1])

for i in arr:
  print(i[0], end=' ')