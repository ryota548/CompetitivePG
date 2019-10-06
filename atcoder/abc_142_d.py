import math

a, b = [int(i) for i in input().split()]

cf = []

for i in range(2, min(a,b)+1):
  if a % i == 0 and b % i == 0:
    cf.append(i)

# print(cf)
ans = 0
limit = math.sqrt(cf[-1])
for k in cf:
  for j in range(2, dest):
    if k % j == 0:
      so = False
  if so:
    ans += 1
  so = True
  

print(ans+1)