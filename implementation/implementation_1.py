n = int(input())
direction = input().split()
x = 1
y = 1

for i in direction:
  if i=="L":
    if y>1:
      y -=1
    
  elif i=="R":
    if y<n:
      y +=1

  elif i=="U":
    if x>1:
      x -= 1

  elif i=="D":
    if x<n:
      x += 1

print(x, y)