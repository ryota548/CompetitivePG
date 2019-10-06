n = int(input())
A = [int(i) for i in input().split()]

pre = {}
for i in range(0, len(A)):
  pre[A[i]]  = i+1

tmp = sorted(pre.items())

ans = []
for tp in tmp:
  ans.append(str(tp[1]))
print(' '.join(ans))