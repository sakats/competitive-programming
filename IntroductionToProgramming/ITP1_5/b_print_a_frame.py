num_list = []

while True:
    H, W = (int(x) for x in input().split())
    if (not H) and (not W):
        break
    num_list.append([H, W])

# print(num_list)

for i in num_list:
    for h in range(i[0]):
        for w in range(i[1]):
            if w == i[1] - 1:
                print("#")
            elif h == 0 or h == i[0] - 1 or w == 0:
                print("#", end="")
            else:
                print(".", end="")
    print("")
