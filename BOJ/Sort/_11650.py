# 좌표 정렬하기
n = int(input())
input_cor = input().split()
arr=[]

for _ in range(n-1):
  input_data = input().split()
  arr.append((int(input_data[0]), int(input_data[1])))

arr.append((int(input_cor[0]), int(input_cor[1])))

arr = sorted(arr, key= lambda x:x[1])
arr = sorted(arr, key= lambda x:x[0])

for i in arr:
  print(i[0], i[1])