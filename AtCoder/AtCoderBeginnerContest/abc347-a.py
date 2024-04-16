n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in a:
    if k <= i and i % k == 0:
        print(i // k, end=" ")
