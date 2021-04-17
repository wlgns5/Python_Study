from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  queue = deque([start])

  # 현재 노드를 방문 처리
  visited[start] = True

  # 큐가 빌 때까지 반복
  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

# 각 노드가 연결된 접오를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)