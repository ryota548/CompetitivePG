N, M = [int(i) for i in input().split()]
edges = [set() for _ in range(N)]
visited = [0]*N
ans = 0

for i in range(M):
  u, v = [int(i) for i in input().split()]
  u, v = u - 1, v - 1
  print(u, v)
  edges[u].add(v)
  edges[v].add(u)
  print(edges)

def dfs(node, parent):
  visited[node] = 1
  for e in edges[node]:
    if e != parent and (visited[e] == 1 or dfs(e, node) == 0):
      return 0
  return 1

for i in range(N):
  if visited[i] == 0:
    ans+=dfs(i, -1)

print(ans)