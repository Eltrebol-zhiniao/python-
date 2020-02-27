

def jiujiu()  :
    """wodemaya"""


    q = 1
    b = 1
    a = 1
    while q <= 9 :
        a = 1
        while b <= q :
            print("%d*%d=%d"%(a,b,a*b),end ="\t")
            a += 1
            if a > b :
                b += 1
                print()
                break
        q += 1