num_list = []

while True:
    x, y = (int(x) for x in input().split())
    if (not x) and (not y):
        break
    else:
        num_list.append([x, y])

for i in num_list:
    for x in range(i[0]):
        for y in range(i[1]):
            print("#", end="")
        print()
    print()
