a, b = [int(i) for i in input().split()]

ans = 0
for i in range(2):
  if a > b:
    ans += a
    a -= 1
  else:
    ans += b
    b -= 1

print(ans)