S = input()

list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
count = [0]*101

for i,w in enumerate(list):
    count[S.count(w)] += 1

del count[0]

for c in count:
    if c != 0 and c != 2:
        print("No")
        exit()
print("Yes")
