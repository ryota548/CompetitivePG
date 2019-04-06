size = int(input())
dots = []
for i in range(size):
  dot = [int(x) for x in input().split()]
  dots.append(dot)
answer = 0

for i in range(size-1):
  for j in range(i+1, size):
    tmp = ((dots[j][0] - dots[i][0])**2 + (dots[j][1] - dots[i][1])**2)**0.5
    if answer < tmp:
      answer = tmp

print(answer)
