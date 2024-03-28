import collections
s = input()
c = collections.Counter(s)

ans = 0
j = 0
for i in "abcdefghijklmnopqrstuvwxyz":
    ans += c[i]*(len(s)-c[i])
    if c[i] >= 2:
        j = 1
ans = ans // 2 + j
print(ans)
