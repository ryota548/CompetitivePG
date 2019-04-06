n, y = [int(i) for i in input().split()]
noAnswer = True
count = 0
for i in range(n+1):
  if noAnswer != True:
      break
  for j in range(n+1):
    k = int(y/1000) - i*10 - j*5
    if k>=0 and n==i+j+k:
      noAnswer = False
      print("{} {} {}".format(i, j, k))
      break

if noAnswer:
  print("-1 -1 -1")