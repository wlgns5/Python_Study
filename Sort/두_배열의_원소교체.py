# p182
n, k = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(k):
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]

print(sum(A))
