# 소트인사이드
arr=list(map(int, input()))

arr = sorted(arr, reverse=True)

for i in arr:
  print(i, end='')