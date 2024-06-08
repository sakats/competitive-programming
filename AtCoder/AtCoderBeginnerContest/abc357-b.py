S = input()

low = sum(map(str.islower, S))
upp = sum(map(str.isupper, S))

if low < upp:
    print(S.upper())
else:
    print(S.lower())
