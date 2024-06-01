N,L,R = list(map(int, input().split()))

ans = []
for n in range(N):
    ans.append(n+1)

ans[L-1:R] = reversed(ans[L-1:R])
for a in ans:
    print(a, end=" ")
