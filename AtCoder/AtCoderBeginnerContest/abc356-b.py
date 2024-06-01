N,M = list(map(int, input().split()))
A = input().split()
X = []
for n in range(N):
    X.append(input().split())

for m in range(M):
    s = 0
    for n in range(N):
        s += int(X[n][m])
    if int(A[m]) > s:
        print("No")
        exit()

print("Yes") 
