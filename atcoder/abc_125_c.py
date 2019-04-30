from fractions import gcd
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
A = [0] + A + [0]
print(A)

l = list(accumulate(A, gcd))
print(l)

r = list(reversed(list(accumulate(reversed(A), gcd))))
print(list(accumulate(reversed(A), gcd)))
print(r)

ans = max(gcd(li, ri) for li, ri in zip(l[:-2], r[2:]))
for li, ri in zip(l[:-2], r[2:]):
  print(li, ri)

print(ans)