n, k = [int(i) for i in input().split()]
s = list(input())

zero = []
cnt = 0
for i in range(n):
  if s[i] == '0':
    if s[i-1] == s[i]:
      zero[cnt] = i
    else:
      cnt += 1
      zero[cnt] = i

print(zero)
