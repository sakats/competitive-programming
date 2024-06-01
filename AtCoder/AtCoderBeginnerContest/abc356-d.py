N,M = list(map(int, input().split()))

ans = int(0)
for n in range(N):
    print(int(int(n+1)&int(M)).bit_count())
    ans += int(int(n+1)&int(M)).bit_count()

print(ans % 998244353)
