num_list = []

while True:
    x = int(input())
    if not x:
        break
    num_list.append(x)

for p in num_list:
    print(sum(map(int, str(p))))
