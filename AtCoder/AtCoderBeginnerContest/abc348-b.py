import math
N = int(input())
I = []
for i in range(N):
    I.append(list(map(int,input().split())))

U = []
for n in range(N):
    max_distance = 0
    ans = -1
    for m in range(N):
        distance = math.sqrt((I[n][0]-I[m][0])**2+(I[n][1]-I[m][1])**2)
        if max_distance < distance:
            max_distance = distance
            ans = m
    print(ans+1)
