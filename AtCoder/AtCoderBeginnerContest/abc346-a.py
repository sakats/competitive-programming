n = int(input())
a = list(map(int, input().split()))

for b in range(n-1):
    print(a[b]*a[b+1], end=" ")
