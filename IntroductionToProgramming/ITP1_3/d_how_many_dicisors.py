a, b, c = (int(x) for x in input().split())

counter = 0

for n in range(1, c+1):
    if c % n == 0 and n >= a and n <= b:
        counter += 1

print(counter)
