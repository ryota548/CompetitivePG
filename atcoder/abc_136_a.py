a, b, c = [int(i) for i in input().split()]

result = b + c - a
if result > 0:
  print(result)
else:
  print(0)