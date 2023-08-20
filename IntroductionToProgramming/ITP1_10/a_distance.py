import math

x1, y1, x2, y2 = (float(x) for x in input().split())

a = {'x': x1, 'y': y1}
b = {'x': x2, 'y': y2}
dist = math.sqrt(math.pow(a['x'] - b['x'], 2) + math.pow(a['y'] - b['y'], 2))

print(f"{dist:.20f}")
