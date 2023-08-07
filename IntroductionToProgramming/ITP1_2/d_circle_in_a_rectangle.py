W, H, x, y, r = (int(x) for x in input().split())

if W >= (x + r) >= r and H >= (y + r) >= r:
    print("Yes")
else:
    print("No")
