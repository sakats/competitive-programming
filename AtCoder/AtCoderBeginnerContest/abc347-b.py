s = input()
ans = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        ans.add(s[i:j])
print(len(ans))
