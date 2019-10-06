n, k = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]

ans = 0
for i in h:
  if (i >= k):
    ans += 1

print(ans)