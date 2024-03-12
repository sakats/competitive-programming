a, b = (int(x) for x in input().split())  

for i in range(10):
    if a+b != i:
        print(i)
        break
