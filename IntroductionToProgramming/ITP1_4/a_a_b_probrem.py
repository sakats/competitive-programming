a, b = (int(x) for x in input().split())

d = a // b
r = a % b
f = a / b

# For f, the output should not contain an 
# absolute error greater than 10-5.
print(f"{d} {r} {f:.20f}")
