H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

total_white = 0
for i in s:
  total_white += i.count(".")

sh = 0
sw = 0
gh = H-1
gw = W-1

s[sh][sw] = 0
q = [[sh, sw]]
min_path = 0

while len(q) > 0:
  h, w = q.pop(0)
  if h == gh and w == gw:
    min_path = s[h][w]
    print(total_white - min_path -1)
    exit()
  for dh, dw in ([0, 1], [0, -1], [1, 0], [-1, 0]):
    if 0 <= h + dh < H and 0 <= w + dw < W:
      if s[h+dh][w+dw] == ".":
        s[h+dh][w+dw] = s[h][w] + 1
        q.append([h+dh, w+dw])

print(-1)
