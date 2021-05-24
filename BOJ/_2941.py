# 크로아티아 알파벳
import sys

s = sys.stdin.readline().rstrip()
a = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}

cnt = 0
for i in a:
    s = s.replace(i, '0')

print(len(s))
