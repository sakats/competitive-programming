n = int(input())
a = list(map(int, input().split()))
m = int(input()) 
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))
sum = set(x)

for i in a:
    for j in b:
        for k in c:
            sum.discard(i+j+k)

for y in x:
    if y in sum:
        print("No")
    else :
        print("Yes")

