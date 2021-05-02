# 수 정렬 하기
n = int(input())
arr=[]
for _ in range(n):
  arr.append(int(input()))

arr = sorted(arr, reverse)

for i in arr:
  print(i)