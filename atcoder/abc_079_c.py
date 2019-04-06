s = input()

for i in range(1<<3):
  x = int(s[0])
  y = s[0]
  for j in range(3):
    if ((i>>j)&1) == 0:
      x += int(s[j+1])
      y += "+" + s[j+1]
    else:
      x -= int(s[j+1])
      y += "-" + s[j+1]
  if x == 7:
    print(y+"=7")
    break
