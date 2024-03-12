a = []
n = int(input())
a.append(n)

if n == 0:
    print(n)
    exit()

while True:
    n = int(input())
    a.append(n)
    if n == 0:
        break

a.reverse()
print(*a, sep="\n")
