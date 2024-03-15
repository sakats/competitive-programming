q = int(input())
a = []
for i in range(q):
    n,x = list(map(int, input().split()))
    if n == 1:
        a.append(x)
    if n == 2:
        print(a[-x])
