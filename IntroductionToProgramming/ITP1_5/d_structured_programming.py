n = int(input())

for x in range(1, n+1):
    if(x % 3 == 0 or x % 10 == 3):
        print(f"{x} ", end="")
        continue
    for y in range(len(str(x))):
       if(x // (10 ** y)) % 10 == 3:
        print(f"{x} ", end="")
        break
