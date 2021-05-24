import sys

N, M = map(int, sys.stdin.readline().split())

aN=[]
aM=[]
result=[]
for _ in range(N):
    aN.append(sys.stdin.readline().rstrip())

for _ in range(M):
    aM.append(sys.stdin.readline().rstrip())

result = sorted(list(set(aN).intersection(set(aM))))

print(len(result))
print('\n'.join(result))
