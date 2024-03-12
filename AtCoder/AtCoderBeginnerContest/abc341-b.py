n = int(input())
a = list(map(int, input().split()))

s = []
for _ in range(n-1):
    s.append(list(map(int, input().split())))

for i in range(n):
    if i != n-1:
        tmp = a[i]
        a[i] = a[i] % s[i][0]
        a[i+1] += (tmp // s[i][0]) * s[i][1]

print(a[n-1])
