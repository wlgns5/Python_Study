# p201

n, m = map(int, input().split())
arr=list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(arr)

# 이진 탐색 수행
result = 0
while (start <= end):
  total = 0
  mid = (start+end) // 2

  for i in arr:
    if i > mid:
      total += i - mid
  
  # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
  if total < m:
    end = mid-1
  
  # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
  else:
    result = mid
    start = mid+1

print(result)
