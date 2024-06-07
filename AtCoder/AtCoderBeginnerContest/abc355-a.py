A, B = input().split()
ans = -1

list = [1,2,3]
list.remove(int(A))
if list.count(int(B)) == 1:
    list.remove(int(B))

if len(list) == 1:
    ans = list[0]

print(ans)
