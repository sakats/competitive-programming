num_list = []

while True:
    x, y = (int(x) for x in input().split())
    if (not x) and (not y):
        break
    elif x >= y:
        num_list.append([y, x])
    else:
        num_list.append([x, y])

for i in num_list:
    print(f"{i[0]} {i[1]}")
