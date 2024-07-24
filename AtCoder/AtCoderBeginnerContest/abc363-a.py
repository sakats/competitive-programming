R = int(input())

ans = 0
for i in range(100, 400, 100):
    if R < i:
        ans = i - R
        break

print(ans)