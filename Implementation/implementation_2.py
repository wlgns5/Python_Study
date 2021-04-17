h = int(input())
result = 0

for hour in range(h+1):
  for m in range(60):
    for s in range(60):
      if "3" in str(hour) or "3" in str(m) or "3" in str(s):
        result += 1

print(result)