n, m = map(int, input().split())

result = 0
minValue = 0

for i in range(n):
  data = list(map(int, input().split()))
  
  if (min(data) > minValue):
    minValue = min(data)

print(minValue)