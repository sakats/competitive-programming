while True:
    m,f,r=map(int,input().split())
    if m<0 and f<0 and r<0:
        break
    if m<0 or f<0:
        print("F")
    elif m+f>=80:
        print("A")
    elif m+f>=65:
        print("B")
    elif m+f>=50:
        print("C")
    elif m+f>=30:
        if r>=50:
            print("C")
        else:
            print("D")
    else:
        print("F")
