a = int(input())

h = a // 3600
m = a % 3600 // 60 
s = a % 60

# 愚直に考えた解法
# m = (a - 3600*h) // 60

print(f"{h}:{m}:{s}")
