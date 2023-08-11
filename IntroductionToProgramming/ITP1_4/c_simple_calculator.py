list = []

while True:
    a = input().split()
    if a[1] == "?":
        break
    list.append(a)

for i in list:
    if i[1] == "/":
        print(f"{int(i[0]) // int(i[2])}")
    elif i[1] == "*":
        print(f"{int(i[0]) * int(i[2])}")
    elif i[1] == "-":
        print(f"{int(i[0]) - int(i[2])}")
    elif i[1] == "+":
        print(f"{int(i[0]) + int(i[2])}")
