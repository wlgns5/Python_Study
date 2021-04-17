N=1260
coin=[500, 100, 50, 10]
give=[]
for i in coin:
  give.append(N // i)
  N%=i

print(N)
print(give)