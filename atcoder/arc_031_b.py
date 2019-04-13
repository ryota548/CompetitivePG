a = [list(input()) for _ in range(10)]

def dfs(a, x, y):
  for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    if 0 <= x + dx < 10 and 0 <= y + dy < 10:
      if a[y+dy][x+dx] == 'o':
        a[y+dy][x+dx] = 'x'
        dfs(a, x+dx, y+dy)

def island(a, x, y):
  dfs(a, x, y)
  return all(all(x == 'x' for x in l) for l in a)

def solve():
  for y in range(10):
    for x in range(10):
      if a[y][x] == 'x':
        a2 = [l[:] for l in a]
        if island(a2, x, y):
          return True

print('YES' if solve() else 'NO')