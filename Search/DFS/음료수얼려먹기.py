# 방문 하기만 하면 True를 return 해서 result 값이 1 증가
# 방문하고 나서 인접한 나머지를 모두 1로 만듦
# for문들 돌면서 1인 곳은 바로 0을 return 하므로
# 중복으로 체크되는 것을 걱정하지 않아도 됨 방문 하기만 하면 True를 return 해서 result 값이 1 증가
# 방문하고 나서 인접한 나머지를 모두 1로 만듦
# for문들 돌면서 1인 곳은 바로 0을 return 하므로
# 중복으로 체크되는 것을 걱정하지 않아도 됨

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))
  

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  if x <= -1 or x >=n or y <= -1 or y >= m:
    return False
  
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True

  return False

result = 0

for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1

print(result)
