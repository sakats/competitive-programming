num_list = []

while True:
    W, H = (int(x) for x in input().split())
    if (not W) and (not H):
        break
    num_list.append([W, H])

for i in num_list:
    for w in range(i[0]):
        for h in range(i[1]):
            if (w+h) % 2:
                print(".", end="")
            else :
                print("#", end="")
            if h == i[1]-1:
                print("")
    print("")
