n = int(input())
v = input().split()
c = input().split()

vc = []
for i in range(n):
  vc.append(int(v[i]) - int(c[i]))

answer = 0
for i in vc:
  if i > 0:
    answer += i

print(answer)
