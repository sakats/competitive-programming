from math import sin, cos, pi, sqrt

a, b, C = map(int, input().split())

S= a * b * sin(C * pi / 180) / 2
c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(C * pi / 180))
h = 2 * S / a

print(S)
print(a + b + c)
print(h)
