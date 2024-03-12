n = int(input())

a = []
for i in range(n):
    a.append(input().split())

ans = []
for i in a:
    for n,j in enumerate(i):
        if int(j) == 1:
            ans.append(int(n+1))
    print(*ans)
    ans.clear()
