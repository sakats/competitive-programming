w,b = list(map(int, input().split()))

s = "wbwbwwbwbwbw"*20
for i in range(12):
    p = s[i:i+w+b]
    if p.count("w") == w and p.count("b") == b:
        print("Yes")
        exit()
print("No")
