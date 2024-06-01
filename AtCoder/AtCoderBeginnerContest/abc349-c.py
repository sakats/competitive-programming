S = input()
T = input()

if T[2] == "X":
    T = T.removesuffix("X")

f = [False]*len(T)
s = 0
for i,t in enumerate(T.lower()):
    if S[s:].count(t) > 0:
        f[i] = True
        s = S[s:].find(t)
        s += 1

if all(f) :
    print("Yes")
else:
    print("No")
