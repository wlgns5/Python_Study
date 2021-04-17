n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1


arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  
  if direction == -1:
    direction = 3


count = 1
block = 0




while True:
  
  turn_left()
  
  tempx = x + dx[direction]
  tempy = y + dy[direction]

  if d[tempx][tempy] == 0 and arr[tempx][tempy] == 0:
    d[tempx][tempy]==1
    x = tempx
    y = tempy
    count += 1
   
    continue
  else:
    block += 1
  
  if block == 4:
    tempx = x - dx[direction]
    tempy = y - dy[direction]

    if arr[tempx][tempy]==0:
      x = tempx
      y = tempy
        
    else:
      break
    
    block=0

print(count)