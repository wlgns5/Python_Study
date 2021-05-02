# 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
a = [0] * 10001

for _ in range(n):
  input_data=int(sys.stdin.readline())
  a[input_data] += 1

for i in range(len(a)):
  if a[i]==0:
    continue
  for _ in range(a[i]):
    print(i)

  

