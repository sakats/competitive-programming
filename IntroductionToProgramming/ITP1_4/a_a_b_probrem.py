a, b = (int(x) for x in input().split())

d = a // b
r = a % b
f = a / b

print(f"{d} {r} {f:.20f}")
