s = list(input())

if len(s) == 1:
  print(0)
  exit()

ans = 0

for i in range(1, len(s)):
  if s[i-1] == s[i]:
    ans += 1
    if s[i] == '0':
      s[i] = '1'
    else:
      s[i] = '0'
  else:
    prev = s[i]

print(ans)