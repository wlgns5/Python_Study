def BinarySearch(arr, start, end, target):
  if start > end:
    return None
  
  mid = (start+end) // 2
  
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return BinarySearch(arr, start, mid-1, target)
  else:
    return BinarySearch(arr, mid+1, end, target)
  

n, target = list(map(int, input().split()))
arr=list(map(int, input().split()))

result = BinarySearch(arr, 0, n-1, target)
if result==None:
  print("원소가 존재하지 않습니다")
else:
  print(result+1)