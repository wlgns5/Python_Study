# p 197

def binary_search(array, target, start, end):
  if start > end:
    return None;
  mid = (start+end) // 2
  
  if array[mid] == target:
    return mid

  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)

  else:
    return binary_search(array, target, mid+1, end)

N = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())
x = list(map(int, input().split()))

for i in x:
  if binary_search(array, i, 0, M) == None:
    print("No", end=' ')
  else:
    print("Yes", end=' ')