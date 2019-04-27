R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for _ in range(R)]

c[sy-1][sx-1] = 0
q = [[sy-1, sx-1]]

while len(q) > 0:
  y, x = q.pop(0)
  if y == gy-1 and x == gx-1:
    print(c[y][x])
    exit()
  for dy, dx in ([0, 1], [0, -1], [1, 0], [-1, 0]):
    if c[y+dy][x+dx] == '.':
      c[y+dy][x+dx] = c[y][x] + 1
      q.append([y+dy, x+dx])