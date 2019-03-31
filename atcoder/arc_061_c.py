s = input()
n = 0
ans = 0
for n in range( 1 << len(s) -1):
    tmp = 0
    for i in range(len(s) - 1):
        if n & (1 << i):
            ans += int(s[tmp:i + 1])
            tmp = i + 1
    if tmp < len(s):
        ans += int(s[tmp:])
print(ans)