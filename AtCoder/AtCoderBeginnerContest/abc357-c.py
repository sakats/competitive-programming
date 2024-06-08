N = int(input())

if N == 0:
    print("#")
    exit()

for a in range(3**N):
    for b in range(3**N):
        # ①真ん中ならしろで埋める
        if a <= 3**N/3 and a >= 2*3**N/3 and b <= 3**N/3 and b >= 2*3**N/3:
            print(".", end="")
        # 1個前のグリッドに該当する、白の条件
        if 0:
            print(".", end="")
        else:
            print("#", end="")
        
        # 端っこで改行
        if b != 0 and b == 3**N-1:
            print()
