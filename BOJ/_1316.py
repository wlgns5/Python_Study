# 그룹 단어 체커
import sys

n = int(input())
cnt = 0

for _ in range(n):
    s = sys.stdin.readline()
    flag = True

    arr = []
    for i in range(len(s)):
        if i+1 == len(s):
            break

        prev = s[i]
        cur = s[i+1]

        if prev != cur:
            if prev in arr:
                flag = False
                break
            arr.append(prev)

    if flag:
        cnt += 1

print(cnt)
